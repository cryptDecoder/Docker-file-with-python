from flask import Flask

app = Flask(__name__)


@app.route("/welcome")
def welcome():
    return "Welcome to My python flask API . . ."


@app.route("/")
def hello():
    return "Hello Flask how are you?"


if __name__ == "__main__":
    app.run(debug=True)
