# flask_web (Unfinish Readme)
flask practices

## P01 Basic Introduction
```
pip install flask
```
- setting
  - debug=True
  - threaded=True
 
- Dynamic route
  
- Status Code
  - default: 200
  - abort (client: 4xx, server: 5xx)
  - redirect: 302
- statistics
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
- get_request
- 

## P02 Manager
```
pip install flask-script
```
- runserver
- assign local url and port
-

## P03 Macro

## P04 Templates
- Front-end(The Jinja2 template engine) and Back-end connection


- flask-bootstrap
```
pip install flask-bootstrap
```

### Demo
```
$python manage.py runserver
```
- http://[root]/
- http://[root]/users
- http://[root]/user/<name>
- http://[root]/tests
- http://[root]/

### References
- Flask 基礎知識與實作 part 1 by 毛毛, Alicia
https://tw.pyladies.com/~maomao/1_flask.slides.html#/3/39

- 《Flask Web開發：基於Python的Web應用開發實戰》筆記二 https://www.itread01.com/content/1550842828.html

- Flask Web開發學習筆記 https://www.jianshu.com/p/417bcbad82fb
