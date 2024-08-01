#!/usr/bin/env python3
"""
Password Encryption Module
"""

import bcrypt
from typing import Union


def hash_password(password: str) -> bytes:
    """
    Hashes a password and returns the hashed password in bytes
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that the provided password matches the hashed password
    """
    return bcrypt.checkpw(password.encode(), hashed_password)


if __name__ == "__main__":
    # Test the hash_password and is_valid functions
    password = "MyAmazingPassw0rd"
    hashed_password = hash_password(password)
    print(f"Hashed password: {hashed_password}")
    print(f"Password is valid: {is_valid(hashed_password, password)}")
