#!/usr/bin/env python3
""" This module contains the BasicAuth class for Authentication """
from api.v1.auth.auth import Auth
from models.user import User
from base64 import b64decode
from typing import Tuple, TypeVar


class BasicAuth(Auth):
    """ Basic Auth subclass of Auth """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Returns Base64 section of auth header """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split("Basic ", 1)[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """ Returns utf-8 decoded base64 header """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_base64 = b64decode(base64_authorization_header)
            return decoded_base64.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """ Returns User email and password """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)

        return tuple(decoded_base64_authorization_header.split(":"))

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ Returns User Instance based on credentials """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        user_list = User.search({'email': user_email})

        if len(user_list) == 0:
            return None

        for user in user_list:
            if user.email == user_email:
                found_user = user
            else:
                return None

        if not found_user.is_valid_password(user_pwd):
            return None

        return found_user
