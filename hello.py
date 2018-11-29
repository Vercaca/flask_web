# hello.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World</h1>"

@app.route("/error")
def error():
    raise RuntimeError

@app.route("/users")
def get_users():
    users = ["Maomao", "Alicia"]
    resp = ["<p>{}</p>".format(user) for user in users]
    resp = "\n".join(resp)

    return resp


if __name__ == "__main__":
    app.run(debug=True)
