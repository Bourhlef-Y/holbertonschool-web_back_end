#!/usr/bin/env python3
""" Module of Index views
This module contains all the views for the API index routes,
including status, stats, and error testing endpoints.
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Returns:
        dict: Status of the API with message "OK"
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Returns:
        dict: Count of objects by type
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized_endpoint():
    """ GET /api/v1/unauthorized
    Raises:
        401: Unauthorized error for testing purposes
    """
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden():
    """ GET /api/v1/forbidden
    Raises:
        403: Forbidden error for testing purposes
    """
    abort(403)
