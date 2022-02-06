#!/usr/bin/python3
"""route /status on the object app_views that returns a JSON:
"status": "OK"""
from api.v1.views import app_views
from flask import jsonify, Flask
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """route /status on the object app_views that returns a JSON"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def counter():
    """endpoint that retrieves the number of each objects by type"""
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("cities"),
                    "places": storage.count("places"),
                    "reviews": storage.count("reviews"),
                    "states": storage.count("states"),
                    "users": storage.count("users")})
