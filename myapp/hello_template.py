from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def get_user(name):
    return render_template("user.html", name=name)


@app.route("/test")
def test():
    mydict = {"key": "This is a secret"}
    mylist = [1, 2, 3, 4]
    myintvar = 0

    class Myobj():
        def method1(self):
            return "I'm a instance method."

        @staticmethod
        def method2():
            return "I'm a static method."

        @classmethod
        def method3(cls, value):
            return "I'm a class method, get value {}".format(value)

    context = {
        "mydict": mydict,
        "mylist": mylist,
        "myintvar": myintvar,
        "instance": Myobj(),
        "class": Myobj,
        "code": "<h1>hey hey</h1>"
    }

    return render_template("test_variable_types.html", **context)
