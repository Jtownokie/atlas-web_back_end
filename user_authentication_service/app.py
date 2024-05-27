#!/usr/bin/env python3
"""
Route module for Basic Flask App
"""
from flask import Flask, jsonify, abort, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
