#!/usr/bin/python3
"""route /status on the object app_views that returns a JSON:
"status": "OK"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.place import Place
from models.review import Review
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity


@app_views.route('/status', strict_slashes=False)
def status():
    """route /status on the object app_views that returns a JSON"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def counter():
    """endpoint that retrieves the number of each objects by type"""
    return jsonify({"amenities": storage.count(Amenity),
                    "cities": storage.count(City),
                    "places": storage.count(Place),
                    "reviews": storage.count(Review),
                    "states": storage.count(State),
                    "users": storage.count(User)})
