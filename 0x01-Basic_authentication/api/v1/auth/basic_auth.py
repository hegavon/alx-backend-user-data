#!/usr/bin/env python3
"""
Definition of class BasicAuth
"""
import base64
from typing import Optional, Tuple
from .auth import Auth
from models.user import User
import logging

class BasicAuth(Auth):
    """ Implement Basic Authorization protocol methods
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> Optional[str]:
        """
        Extracts the Base64 part of the Authorization header for a Basic
        Authorization.

        Args:
            authorization_header (str): The Authorization header.

        Returns:
            Optional[str]: The Base64 token, or None if not valid.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        token = authorization_header.split(" ")[-1]
        return token

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> Optional[str]:
        """
        Decode a Base64-encoded string.

        Args:
            base64_authorization_header (str): The Base64-encoded header.

        Returns:
            Optional[str]: The decoded string, or None if decoding fails.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header.encode('utf-8'))
            return decoded.decode('utf-8')
        except Exception as e:
            logging.error(f"Decoding error: {e}")
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
    ) -> Tuple[Optional[str], Optional[str]]:
        """
        Returns user email and password from Base64 decoded value.

        Args:
            decoded_base64_authorization_header (str): The decoded header.

        Returns:
            Tuple[Optional[str], Optional[str]]: User email and password, or None.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(":", 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> Optional[User]:
        """
        Return a User instance based on email and password.

        Args:
            user_email (str): The user's email.
            user_pwd (str): The user's password.

        Returns:
            Optional[User]: A User instance if valid, otherwise None.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
            return None
        except Exception as e:
            logging.error(f"User search error: {e}")
            return None

    def current_user(self, request=None) -> Optional[User]:
        """
        Returns a User instance based on a received request.

        Args:
            request: The Flask request object.

        Returns:
            Optional[User]: A User instance if valid, otherwise None.
        """
        auth_header = self.authorization_header(request)
        if auth_header:
            token = self.extract_base64_authorization_header(auth_header)
            if token:
                decoded = self.decode_base64_authorization_header(token)
                if decoded:
                    email, password = self.extract_user_credentials(decoded)
                    if email:
                        return self.user_object_from_credentials(
                            email, password
                        )
        return None
