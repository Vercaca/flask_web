from . import main
from app import tasks


@main.route('/run', methods=['GET'])
def run():
    tasks.ping.delay()
    return 'ok'


@main.route('/', methods=['GET'])
def index():
    return 'ok'
