# import logging

from flask import Flask

from config import config


def create_app(config_name):

    app = Flask(__name__)

    flask_config = config[config_name]['flask']
    app.config.from_object(flask_config)
    # flask_config.init_app(app)

    from .api import api_bp as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
