#!/usr/bin/env python3
""" This module contains the SessionAuth class for Authentication """
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ SessionAuth Subclass of Auth """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ This Method creates a session id for a user id """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = uuid.uuid4()

        self.user_id_by_session_id[f'{session_id}'] = user_id

        return session_id
