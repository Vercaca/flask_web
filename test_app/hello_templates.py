from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="templates")
app.debug = True

registered_users = ["vansan", "veronica", "vicky"]
stores = [{
    'name': 'Elton\'s first store',
    'items': [{'name': 'my item 1', 'price': 30}],
    },
    {
    'name': 'Elton\'s second store',
    'items':  [{'name': 'my item 2', 'price': 15}],
    },
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    name = name.lower()
    if name not in registered_users:
        name = None
    return render_template("user.html", name=name)


"""
http://127.0.0.1:5000/echo?text=<name>
:return:
"""
@app.route("/echo")
def get_user_with_get():
    user_argent = request.headers.get("User-Agent")
    user_text = request.args.get("text")

    return f"<p>Your browser is {user_argent}</p>" \
        f"<p>echo: {user_text}</p>"


# GET stores
@app.route("/store")
def get_stores():
    return jsonify(stores)


# POST /store data: {name :}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    print(request_data)
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route("/test")
def test():
    my_dict = {"key": "This is a secret"}
    my_list = [1, 2, 3, 4]
    my_int_var = 0

    class MyObj:
        def method1(self):
            return "I'm a instance method."

        @staticmethod
        def method2():
            return "I'm a static method."

        @classmethod
        def method3(cls, value):
            return "I'm a class method, get value {}".format(value)

    context = {
        "my_dict": my_dict,
        "my_list": my_list,
        "my_int_var": my_int_var,
        "my_instance": MyObj(),
        "my_class": MyObj,
        "code": "<h1>hey hey</h1>"
    }

    return render_template("test_variable_types.html", **context)


@app.route("/users")
def users():
    return render_template("users.html", users=registered_users)

