from flask import Flask, send_from_directory
import logging

from server.api import init_api
from json_store import init_store
from server.model import get_model

logging.basicConfig(level=logging.WARNING)

log = logging.getLogger('server')
log.setLevel(logging.DEBUG)
log.info("Startup")
log.info("...create store")
init_store("data", True)
log.info("...create model")
model = get_model()
log.info("...build app")
app = Flask(__name__)

"""
Main routes path.
All routing is client side, and so we just serve up the app.
"""
@app.get("/")
@app.get("/<path:path>")
def home(path = None):
    return send_from_directory('client/public', 'index.html')

"""
Path for all the static files (compiled JS/CSS, etc.)
"""
@app.get("/resource/<path:path>")
def content(path):
    return send_from_directory('client/public', path)

#Load in the controllers from the API:
init_api(app)
    
if __name__ == "__main__":
    app.run(debug=True, port=62537, )
