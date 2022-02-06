#!/usr/bin/python3
"""Index file"""
from api.v1.views import app_views
from flask import Flask, jsonify


@app_views.route('/status')
def status():
    """route /status on the object app_views that returns a JSON"""
    return jsonify({"status": "OK"})
