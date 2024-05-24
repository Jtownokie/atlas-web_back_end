#!/usr/bin/env python3
""" This module contains the BasicAuth class for Authentication """
from api.v1.auth.auth import Auth


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
