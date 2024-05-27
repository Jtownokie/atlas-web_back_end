#!/usr/bin/env python3
"""
Route module for Basic Flask App
"""
from flask import Flask, jsonify, abort, request, make_response, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def app_start() -> str:
    """ GET /
    Return:
      - Basic JSON
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """ GET
    Return:
        - JSON
    """
    user = AUTH.get_user_from_session_id(request.cookies.get("session_id"))
    if user is None:
        abort(403)

    return jsonify({"email": f"{user.email}"}), 200


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ POST
    Return:
        - None
    """
    user_email = request.form.get("email")
    user_pwd = request.form.get("password")

    try:
        AUTH.register_user(user_email, user_pwd)
        return jsonify({"email": f"{user_email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ POST
    Return:
        - None
    """
    user_email = request.form.get("email")
    user_pwd = request.form.get("password")

    if AUTH.valid_login(user_email, user_pwd) is False:
        abort(401)

    session_id = AUTH.create_session(user_email)

    response = make_response(
        jsonify({"email": f"{user_email}", "message": "logged in"})
    )
    response.set_cookie("session_id", session_id)

    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ DELETE
    Return:
        - None
    """
    user = AUTH.get_user_from_session_id(request.cookies.get("session_id"))
    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
