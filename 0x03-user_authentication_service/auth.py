#!/usr/bin/env python3
# auth.py

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt and returns the hashed password in bytes.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: The salted hash of the password.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password
