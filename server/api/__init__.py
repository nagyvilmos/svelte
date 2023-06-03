from flask import Blueprint, abort, json
import random

from .auth import auth_init
from .todo import todo_init

api = Blueprint('api',__name__, url_prefix="/api")

# don't know API catch:
@api.route("")
@api.route("/<path:path>")
def bad_request(path = None):
    abort(404)


@api.route("/rand")
def hello():
    return json.jsonify({"random": random.randint(0, 100)})

def init_api(app):
    auth_init(api)
    todo_init(api)
    app.register_blueprint(api)
