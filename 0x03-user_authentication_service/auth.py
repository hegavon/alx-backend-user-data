#!/usr/bin/env python3
"""
Auth module to interact with the authentication database.
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Initialize a new Auth instance."""
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """
        Hashes a password using bcrypt and returns the hashed password in bytes

        Args:
            password (str): The password to be hashed.

        Returns:
            bytes: The salted hash of the password.
        """
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user if the email is not already taken.

        Args:
            email (str): The user's email address.
            password (str): The user's password.

        Returns:
            User: The User object of the newly created user.

        Raises:
            ValueError: If a user with the same email already exists.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = self._hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user
