#!/usr/bin/env python3
""" This module contains the BasicAuth class for Authentication """
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import Tuple


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
