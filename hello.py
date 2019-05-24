# hello.py
from time import sleep

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    user_argent = request.headers.get("User-Agent")
    user_name = request.args.get("name")
    # return "<h1>Hello World</h1>"
    return f"<p>Your browser is {user_argent}</p>" \
        f"<p>Your name is {user_name}</p>"


@app.route("/error")
def error():
    raise RuntimeError


@app.route("/users")
def get_users():
    users = ["Maomao", "Alicia"]
    resp = ["<p>{}</p>".format(user) for user in users]
    resp = "\n".join(resp)

    return resp


@app.route("/user/<name>")
def get_user_name(name):
    return "<h1>Hello, {}!</h1>".format(name)


@app.route("/user/<int:uid>")
def get_user_id(uid):
    if isinstance(uid, int):
        return "<h1>Your ID: {}</h1>".format(uid)
    return "<h1>ID should be int</h1>"


@app.route("/user/<path:path>")
def get_user_path(path):
    return "<h1>Path: {}</h1>".format(path)


if __name__ == "__main__":
    app.run(threaded=True, debug=True)
