from flask import Blueprint, json, request
from server.model import get_model

model = None
auth = Blueprint('auth', __name__, url_prefix="/auth")


@auth.route("/login", methods=["GET"])
def login():
    # get the user and password arguments, both must be set.
    # if any other then fail out
    name = request.args.get("name")
    password = request.args.get("password")
    if name is None or password is None:
        return json.jsonify({}), 401
    #[isOkay, rep] = model.users.validate_login(name, password)
    isOkay = True
    rep = {"user": name, "authorised": True}
    if not isOkay:
        return json.jsonify({}), 401
    return json.jsonify(rep)


def auth_init(app):
    global model
    model = get_model()
    app.register_blueprint(auth)
