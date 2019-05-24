# hello.py

from flask import Flask, abort, request, Response, make_response

app = Flask(__name__)

statistic_data = {}

# use before_request to calculate the number of times you buy things
@app.before_request
def statistic():
    if request.path in ["/", "/statistic"]:
        return
    statistic_data[request.path] = statistic_data.setdefault(request.path, 0) + 1


@app.route("/statistic")
def get_statistic():
    return f"statistic_data: {statistic_data}"


@app.route("/")
def index():
    """
    http://127.0.0.1:5000/?name=<name>
    :return:
    """
    user_argent = request.headers.get("User-Agent")
    user_name = request.args.get("name")

    return f"<p>Your browser is {user_argent}</p>" \
        f"<p>Your name is {user_name}</p>"


@app.route("/400")
def bad_request():
    return "<h1>Bad Request</h1>", 400


@app.route("/302")
def redirect():
    return "<h1>Redirect</h1>", 302, {"Location": "http://www.google.com"}


@app.route("/no_cookie")
def no_cookie():
    data = "<h1>This document doesn't carry a cookie!</h1>"
    response = make_response(data)
    return response


@app.route("/has_cookie")
def has_cookie():
    data = "<h1>This document carries a cookie!</h1>"
    # response = make_response(data)
    # response.set_cookie("answer", "42")
    # return response
    headers = {}
    headers["Set-Cookie"] = "answer=45"
    return Response(data, headers=headers)


@app.route("/error")
def error():
    raise RuntimeError


def load_user(uid):
    try:
        uid = int(uid)
        if uid == 1:
            return "Vansan"
        elif uid == 2:
            return "Veronica"
        elif uid == 3:
            return "Vicky"
    except BaseException:
        return

# ## client error: 4xx , server error: 5xx
@app.route("/user/<int:uid>")
def get_user_id(uid):
    # if isinstance(uid, int):
    #     return "<h1>Your ID: {}</h1>".format(uid)
    # return "<h1>ID should be int</h1>"
    user = load_user(uid)
    if not user:
        abort(400, f'No uid: {uid} matches.')
    else:
        return f"<h1>Hello, {user}!</h1>"


@app.route("/user/<path:path>")
def get_user_path(path):
    return "<h1>Path: {}</h1>".format(path)


if __name__ == "__main__":
    app.run(threaded=True, debug=True)
