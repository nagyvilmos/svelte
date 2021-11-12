from flask import Flask
import random

app = Flask(__name__)

@app.route("/api/rand")
def hello():
    return str(random.randint(0, 100))

if __name__ == "__main__":
    app.run(debug=True, port=62537)
