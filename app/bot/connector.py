import requests

from app import bot_config

__auth__header = {'x-gss-bot-authentication': bot_config.bot_key}


def push(url, payload):
    return requests.post(url, headers=__auth__header, json=payload)
