#!/usr/bin/env python3
""" Module of Session Auth views
"""
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def user_login():
    """ POST /api/v1/auth_session/login
    Return:
      - list of all User objects JSON represented
    """
    user_email = request.form.get('email')
    user_password = request.form.get('password')

    if user_email is None:
        return jsonify({"error": "email missing"}), 400
    if user_password is None:
        return jsonify({"error": "password missing"}), 400

    user_list = User.search({'email': user_email})

    if len(user_list) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = user_list[0]

    if not user.is_valid_password(user_password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    response = make_response(user.to_json())
    response.set_cookie(f'{getenv("SESSION_NAME")}', session_id)

    return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def user_logout():
    """ DELETE /api/v1/auth_session/current_user
    Return:
      - empty JSON if the User has been correctly deleted
      - 404 if the User ID doesn't exist
    """
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    else:
        abort(404)
