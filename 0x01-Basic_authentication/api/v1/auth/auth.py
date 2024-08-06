#!/usr/bin/env python3
"""
Definition of class Auth
"""
from flask import request
from typing import List, Optional, TypeVar

User = TypeVar('User')


class Auth:
    """
    Manages the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether a given path requires authentication or not
        Args:
            - path (str): Url path to be checked
            - excluded_paths (List[str]): List of paths that do not require
              authentication
        Return:
            - True if path is not in excluded_paths, else False
        """
        if path is None:
            return True
        elif excluded_paths is None or not excluded_paths:
            return True
        elif path in excluded_paths:
            return False

        for i in excluded_paths:
            if i.startswith(path) or path.startswith(i):
                return False
            if i.endswith("*") and path.startswith(i[:-1]):
                return False

        return True

    def authorization_header(self, request=None) -> Optional[str]:
        """
        Returns the authorization header from a request object
        """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> User:
        """
        Returns a User instance from information from a request object
        """
        return None
