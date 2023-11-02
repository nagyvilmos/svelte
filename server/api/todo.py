from flask import Blueprint, json, request
from server.model import get_model
from json_store.data import Data
import logging;

log = logging.getLogger('todo')
log.setLevel(logging.DEBUG)

dummy_list = Data([
    {'_id': '1', 'user': 'william', 'due': '20230605', 'description': 'blah blah', 'complete': False},
    {'_id': '2', 'user': 'steve', 'due': '20230601', 'description': 'blah', 'complete': True},
    {'_id': '3', 'user': 'alex', 'due': '20230615', 'description': 'blah blah blah', 'complete': False},
    {'_id': '4', 'user': 'william', 'due': '20230612', 'description': 'blah blah blah blah blah', 'complete': True},
    {'_id': '5', 'user': 'steve', 'due': '20230607', 'description': 'blah blah blah blah', 'complete': False},
])
model = None
todo = Blueprint('todo', __name__, url_prefix="/todo")

def build_filter():
    filter=[]
    for (field_name, field_type) in [('user', 'exact'), ('due', 'start'), ('description', 'include'), ('complete', 'exact')]:
        arg_value = request.args.get(field_name)
        if arg_value is None:
            continue
        log.debug(f'{field_name} as {field_type} = {arg_value}')
        def match(name, type, value):
            return {
                'include': lambda row : row.get(name) is not None and (value in row.get(name).lower()),
                'start': lambda row : row.get(name) is not None and (row.get(name)[:len(value)] == value),
                'exact':lambda row : row.get(name) == (value == '1')
            }[type]

        filter.append(match(field_name,field_type,arg_value))

    if len(filter) == 0:
        return None

    def filter_function(row):
        for filter_field in filter:
            match = filter_field(row) 
            if not match:
                return False
        return True
    
    return filter_function
#Create

#Read
@todo.route("/", methods=["GET"])
def get_list():
    filter = build_filter()
    return json.jsonify(dummy_list.list() if filter is None else dummy_list.filter(filter).list())

@todo.route("/<id>", methods=["GET"])
def get_by_id(id):
    for row in dummy_list:
        if row.get('_id') == id:
            return json.jsonify(row)
    return json.jsonify({})

#Update
#Delete

def todo_init(app):
    global model
    model = get_model()
    app.register_blueprint(todo)
