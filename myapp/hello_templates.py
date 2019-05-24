from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")
app.debug = True

registered_users = ["vansan", "veronica", "vicky"]
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    name = name.lower()
    if name not in registered_users:
        name = None
    return render_template("user.html", name=name)


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
