from datetime import datetime

import requests
from celery import Celery
# from app import celery

broker = 'redis://127.0.0.1:6379'
backend = 'redis://127.0.0.1:6379/0'

celery = Celery('my_task', broker=broker, backend=backend)


@celery.task
def ping():
    # res = requests.get('http://bot:8888/')
    # return {'code': res.status_code, 'datetime': str(datetime.now())}
    return {'code': 200, 'datetime': str(datetime.now())}
