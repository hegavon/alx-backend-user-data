#!/usr/bin/env python3
""" API setup module """
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from os import getenv

app = Flask(__name__)
CORS(app)

AUTH_TYPE = getenv('AUTH_TYPE', 'auth')
if AUTH_TYPE == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.errorhandler(401)
def unauthorized(error):
    """Unauthorized handler"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error):
    """Forbidden handler"""
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    """Request filter"""
    if auth is None:
        return
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                      '/api/v1/forbidden/']
    if not auth.require_auth(request.path, excluded_paths):
        return
    if auth.authorization_header(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)


@app.route('/api/v1/status', methods=['GET'])
def status():
    """Returns status OK"""
    return jsonify({"status": "OK"}), 200


@app.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized_endpoint():
    """Raises a 401 Unauthorized error for testing"""
    abort(401)


if __name__ == '__main__':
    app.run(host=getenv('API_HOST', '0.0.0.0'),
            port=int(getenv('API_PORT', 5000)))
