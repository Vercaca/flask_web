from flask import Flask


def create_app(config=None):
    app = Flask(__name__)
    if config is not None:
        app.config.from_pyfile(config)
    # configure your app...
    return app
