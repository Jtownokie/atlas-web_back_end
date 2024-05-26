#!/usr/bin/env python3
""" This module contains the Auth class for Authentication """
from flask import request
from typing import List, TypeVar
from os import getenv


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
        if request is None:
            return None
        elif "Authorization" not in request.headers.keys():
            return None
        else:
            return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """ Checks Current User """
        return None

    def session_cookie(self, request=None):
        """ This Method Returns a cookie value from a request """
        if request is None:
            return None

        return request.cookies.get(f'{getenv("SESSION_NAME")}')
