# import logging

# import redis
from flask import Flask
from celery import Celery
# from celery.signals import worker_process_init, worker_process_shutdown
# from celery.schedules import crontab

from config import config
# from .__version__ import __author__, __copyright__

# redis_pool = None
broker = 'redis://127.0.0.1:6379'
backend = 'redis://127.0.0.1:6379/0'

celery = Celery(__name__, broker=broker, backend=backend)

bot_config = None


def create_app(config_name):
    global bot_config
    bot_config = config[config_name]['bot']

    app = Flask(__name__)

    flask_config = config[config_name]['flask']
    app.config.from_object(flask_config)
    # flask_config.init_app(app)

    celery.config_from_object(config[config_name]['celery'])

    # global redis_pool
    # redis_pool = redis.ConnectionPool.from_url(
    #     bot_config.db_url, decode_responses=True)

    from .api import api_bp as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


# @worker_process_init.connect
# def celery_worker_init(**kwargs):
#     r = redis.StrictRedis(connection_pool=redis_pool)
#     r.set('celery_worker_log', 'running')
#
#
# @worker_process_shutdown.connect
# def celery_worker_shutdown(**kwargs):
#     r = redis.StrictRedis(connection_pool=redis_pool)
#     r.set('celery_worker_log', 'shutdown')
#
#
# @celery.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     from app.bot import handlers
#
#     sender.add_periodic_task(
#         crontab(hour=8, minute=30), handlers.push.s(), name='morning push')
#     sender.add_periodic_task(
#         crontab(hour=11, minute=55), handlers.push.s(), name='lunch push')
#     sender.add_periodic_task(
#         crontab(hour=17, minute=30), handlers.push.s(), name='afternon push')
