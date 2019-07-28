import os
# __redis_pw__ = os.getenv('REDIS_PASSWORD') or ''
# if __redis_pw__:
#     __redis_pw__ = ':{}@'.format(__redis_pw__)
# __redis_local__ = 'redis://{}localhost:6379/'.format(__redis_pw__)
__redis_local__ = 'redis://127.0.0.1:6379/'
# __redis_docker__ = 'redis://{}redis:6380/'.format(__redis_pw__)


class CeleryConfig:
    broker_url = __redis_local__ + '0'
    result_backend = __redis_local__ + '1'

    task_serializer = 'json'
    result_serializer = 'json'
    accept_content = ['json']

    task_eager_propagates = True
    task_ignore_result = False

    timezone = 'Asia/Taipei'  # default UTC
    enable_utc = True
    imports = (  # 指定导入的任务模块
        'app.send_about'
    )


class FlaskConfig:
    # DEBUG = True
    @staticmethod
    def init_app(app):
        pass


class BotConfig:
    bot_id = 'demo_bot'
    bot_key = os.getenv('NO_KEY') or ''
    # db_url = __redis_local__ + '2'


config = {
    'default': {
        'bot': BotConfig,
        'celery': 'app.celeryconfig',
        'flask': FlaskConfig
    },
    # 'docker': {
    #     'bot': BotDockerConfig,
    #     'celery': 'config:CeleryDockerConfig',
    #     'flask': FlaskDockerConfig
    # }
}
