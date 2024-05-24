#!/usr/bin/env python3
""" This module contains the Auth class for Authentication """
from flask import request
from typing import List, TypeVar


class Auth():
    """ This class handles API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Requires Authorization """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        for ex_path in excluded_paths:
            if path in ex_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Returns Auth Head """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Checks Current User """
        return None
