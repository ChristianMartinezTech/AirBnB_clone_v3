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
def teardown_appcontext(self):
    """Removes the sqlalchemy session"""
    storage.close()


if __name__ == "__main__":
    # host_final = getenv('HBNB_API_HOST', '0.0.0.0')
    # port_final = getenv('HBNB_API_PORT', 5000)

    app.run(host=getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(getenv('HBNB_API_PORT', '5000')),
            threaded=True, debug=True)
