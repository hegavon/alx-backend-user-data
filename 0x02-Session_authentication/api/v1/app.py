#!/usr/bin/env python3
"""API entry point for the user data management system."""

import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flasgger import Swagger
from api.v1.views import app_views
from models import storage
from models.user import User  # Import the User model
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth
from api.v1.auth.session_exp_auth import SessionExpAuth
from api.v1.auth.session_db_auth import SessionDBAuth


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
swagger = Swagger(app)

auth = None
auth_type = os.getenv("AUTH_TYPE")

if auth_type == "basic_auth":
    auth = BasicAuth()
elif auth_type == "session_auth":
    auth = SessionAuth()
elif auth_type == "session_exp_auth":
    auth = SessionExpAuth()
elif auth_type == "session_db_auth":
    auth = SessionDBAuth()


@app.before_request
def before_request():
    """Before request handler to manage user authentication."""
    if auth:
        request.current_user = auth.current_user(request)

    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                      '/api/v1/forbidden/', '/api/v1/auth_session/login/']

    if auth and auth.require_auth(request.path, excluded_paths):
        if auth.authorization_header(request) is None and \
                auth.session_cookie(request) is None:
            return jsonify({"error": "Unauthorized"}), 401

        if request.current_user is None:
            return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error):
    """404 Not Found handler."""
    return jsonify({"error": "Not found"}), 404


@app_views.route('/auth_session/login', methods=['POST'],
                 strict_slashes=False)
def auth_session():
    """
    Handle user login and create a session.
    Return:
        dictionary representation of user if found else error message
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(password):
            session_id = auth.create_session(user.id)
            resp = jsonify(user.to_json())
            session_name = os.getenv('SESSION_NAME')
            resp.set_cookie(session_name, session_id)
            return resp

    return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def handle_logout():
    """
    Handle user logout and destroy the session.
    """
    if auth.destroy_session(request):
        return jsonify({}), 200
    return jsonify({"error": "Forbidden"}), 404


if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = os.getenv("API_PORT", "5000")
    app.run(host=host, port=port, threaded=True)
