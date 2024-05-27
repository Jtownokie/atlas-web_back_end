#!/usr/bin/env python3
""" This module contains the SessionAuth class for Authentication """
from api.v1.auth.auth import Auth
from models.user import User
import uuid
from flask import request
from os import getenv


class SessionAuth(Auth):
    """ SessionAuth Subclass of Auth """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ This Method creates a session id for a user id """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[f'{session_id}'] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ This method returns a User ID based on Session ID """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Returns User Instance Based on Cookie Value """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)

        return User.get(user_id)

    def destroy_session(self, request=None):
        """ Deletes User Session/Logs Out """
        if request is None:
            return False
        if not self.session_cookie(request):
            return False

        session_id = request.cookies.get(getenv("SESSION_NAME"))

        if not self.user_id_for_session_id(session_id):
            return False

        del self.user_id_by_session_id[f'{session_id}']
        return True
