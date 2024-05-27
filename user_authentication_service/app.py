#!/usr/bin/env python3
"""
Route module for Basic Flask App
"""
from flask import Flask, jsonify, abort, request


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def app_start() -> str:
    """ GET /
    Return:
      - Basic JSON
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
