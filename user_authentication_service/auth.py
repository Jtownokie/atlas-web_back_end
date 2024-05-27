#!/usr/bin/env python3
""" Auth Class Module """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Returns a hashed, salted password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
