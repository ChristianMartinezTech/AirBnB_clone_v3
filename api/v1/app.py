#!/usr/bin/python3
"""Flask application"""

from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views

# Instanciating Flask in app
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exeption):
    """Removes the sqlalchemy session"""
    storage.close()

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    if host is None:
        host = '0.0.0.0'

    port = getenv('HBNB_API_PORT')
    if port is None:
        port = 5000

    app.run(host=host, port=port, threaded=True, debug=True)
