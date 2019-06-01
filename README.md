# flask_web (Unfinish Readme)
A simple implementaion with Flask API in Python.
(INTRODUCTION HERE!!!)

## P01 Basic Introduction
> /myapp/hello.py
```
pip install flask
```
- Setting
  - debug=True    # backend update your code while server is running
  - threaded=True  # Try it yourself!!
  ```
  from flask import Flask
  
  app = Flask(__name__)
  app.run(threaded=True, debug=True)
  ```
  
- Static route vs. Dynamic route
  - Static route (http://127.0.0.1:xxxx/index)
  ```
  @app.route("/index")
  def index():
      """
      http://127.0.0.1:5000/index
      :return:
      """
      return "<h1>Hello World!</h1>"

  ```
  - Dynamic route (http://127.0.0.1:xxxx/user/[YOUR_NAME])
  ```
  def load_user(user_name):
    if user_name in users:
        return user_name
    else:
        return None
  @app.route("/user/<user_name>")
  def get_user():
    user = load_user()
    if not user:
        abort(400, f'No username: {user_name} matches.')
    else:
        return f"<h1>Hello, {user}!</h1>"
  ```
  
- Status Code
  - default: 200
  - abort (client: 4xx, server: 5xx)
  - redirect: 302
  ```
  @app.route("/302")
  def redirect():
      return "<h1>Redirect</h1>", 302, {"Location": "http://www.google.com"}
  ```
- Statistics
```
statistic_data = {}

@app.before_request
def statistic():
    if request.path in ["/", "/statistic"]:
        return
    statistic_data[request.path] = statistic_data.setdefault(request.path, 0) + 1

@app.route("/statistic")
def get_statistic():
    return f"statistic_data: {statistic_data}"

```
- Cookie
  - Response
  ```
  from flask import Response
  
  @app.route("/has_cookie")
  def has_cookie():
      data = "<h1>This document carries a cookie!</h1>"
      headers = {}
      headers["Set-Cookie"] = "answer=45"
      return Response(data, headers=headers)
  ```
  ```
  
  ```
- GET request (http://127.0.0.1:xxxx/user?name=[YOUR_NAME])
```
"""
http://127.0.0.1:5000/user?name=<name>
:return:
"""
@app.route("/user")
def get_user_with_get():
    user_argent = request.headers.get("User-Agent")
    user_name = request.args.get("name")

    return f"<p>Your browser is {user_argent}</p>" \
        f"<p>Your name is {user_name}</p>"
```
- POST request
```
(TODO)
```

### demo P01
```
python myapp/hello.py
```

***
## P02 Manager
```
pip install flask-script
```
#### to manage your Flask app
> /manage.py
- runserver
- assign local url and port
```
from flask_script import Manager, Server
from myapp.hello import app  # import your app
manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=5566))
```
- add command / option
```
@manager.option('-n', '--name', dest='name', default='joe', help="Your name")
@manager.option('-u', '--url', dest='url', default=None)
def hello(name, url):
    """
    :param name, url:
    :return:
    $ python manage.py hello -n Ver -u Yahoo
    hello, Ver, from Yahoo

    """
    if url is None:
        print(f"hello, {name}")
    else:
        print(f"hello, {name}, from {url}")

@manager.command
def verify(verified=False):
    """
    checks if verified
    :param verified:
    :return None:
\
    $ python manage.py verify -v
    VERIFIED? Yes
    $ python manage.py verify
    VERIFIED? No
    """
    print(f"VERIFIED? {'Yes' if verified else 'No'}")
```
- run in main
```
manager.run()
```

### demo P02
```
python manage.py hello -n Ver -u Yahoo
hello, Ver, from Yahoo
```

***
## P03 Templates
- Front-end(The Jinja2 template engine) and Back-end connection
- flask-bootstrap
```
pip install flask-bootstrap
```
- Back-end connection
  > /myapp/hello_templates.py
  ```
  from flask import render_template
  app = Flask(__name__, template_folder="templates")
  app.debug = True

  @app.route("/")
  def index():
      return render_template("index.html")
  ```
- put your templates (html) into /myapp/templates/
  > /myapp/templates/index.html
  ```
  <html>
      <head>
          <meta charset="UTF-8">
          <title>Hello World</title>
      </head>
      <body>
          <h1>Hello World!</h1>
      </body>
  </html>
  ```
- more usages and variable types can see the codes.

### Demo P03
```
$python manage.py runserver
```

***
## P04 Macro (Like Function)
- you call write a Macro used in html and call by its names
> /myapp/templates/macros.html
Example: 

Customize your macro here
```
<!-- templates/macros.html -->

{% macro render_user(user) %}
    <li>{{ user|title }}</li>
{% endmacro %}
```
Your Front Page
> /myapp/templates/macros.html
```
<!-- templates/test.html -->
{%  import "macros.html" as macros %}
<body>
  <ul>
      {%  for user in users %}
          {{ macros.render_user(user) }}
      {% endfor %}
  </ul>
</body>
```


## References
- [Flask 基礎知識與實作 part 1 by 毛毛, Alicia](https://tw.pyladies.com/~maomao/1_flask.slides.html#/3/39)
- [《Flask Web開發：基於Python的Web應用開發實戰》筆記二](https://www.itread01.com/content/1550842828.html)
- [Flask Web開發學習筆記](https://www.jianshu.com/p/417bcbad82fb)
