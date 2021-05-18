import json
from json.decoder import JSONDecodeError

from flask import Flask
from flask import jsonify
from flask import request

from rengine import Sherlock


# Set up app
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


def read_data(source):
    """
    Reads file that is expected to hold JSON encoded content.
    In case of errors return empty data and list holding error message.
    """
    data = []
    errors = []
    try:
        with open(source) as db:
            content = db.read()
        data = json.loads(content)
    except FileNotFoundError as e:
        errors = [f"Reading {source}, {str(e)}"]
    except JSONDecodeError as e:
        errors = [f"Reading {source}, {str(e)}"]
    except Exception as e:
        errors = [f"Reading {source}, {str(e)}"]

    return data, errors


@app.route("/api/v1/movies/recommend", methods=["GET"])
def recommend():
    """
    Function loads movies from db and returns recommendations.
    """
    MOVIES, errors = read_data("/app/db.json")
    if errors:
        return jsonify({"errors": errors, "status_code": 500}), 500

    sherlock = Sherlock(MOVIES, request.args)
    recommendation = sherlock.recommend()

    return jsonify(recommendation)
