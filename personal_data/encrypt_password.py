#!/usr/bin/env python3
"""
    Password Encryption Module
"""
import typing
import bcrypt


def hash_password(password: str) -> typing.ByteString:
    """ Returns a hashed, salted password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
