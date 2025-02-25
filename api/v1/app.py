#!/usr/bin/python3
"""
flask app for the AirBnB project
"""

from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_db(exception):
    """storage is closed"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    port = getenv("HBNB_API_PORT", "5000")
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    app.run(host=host, port=port, threaded=True)
