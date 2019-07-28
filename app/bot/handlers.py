import logging
import json
# from random import choice
from botbuilder.schema import Activity
from botframework.connector import ConnectorClient
from botframework.connector.auth import (
    MicrosoftAppCredentials,
)
# from app import celery
from celery import Celery
celery = Celery(__name__)
celery.config_from_object("app:CeleryConfig")

from app.bot import connector
# from app.utils import get_about
# from app.db import user, cat, bot, holiday

# __ig_host__ = 'https://www.instagram.com/{}/'
APP_ID = ""
APP_PASSWORD = ""


def __create_reply_activity(activity, text=''):
    print('inside create reply activity')
    reply = {
        'type': 'message',
        'from': activity['recipient'],
        'recipient': activity['from'],
        'conversation': activity['conversation'],
        'channelId': activity['channelId'],
        'text': text,
    }
    url = '{}/v3/conversations/{}/activities'.format(
        activity['serviceUrl'], activity['conversation']['id'])
    print('previous url = {}'.format(url))
    url = activity['serviceUrl']
    print('try url = {}'.format(url))
    return reply, url

    # return Activity(
    #     type='message',
    #     channel_id=request_activity.channel_id,
    #     conversation=request_activity.conversation,
    #     recipient=request_activity.from_property,
    #     from_property=request_activity.recipient,
    #     text=text,
    #     service_url=request_activity.service_url,
    # )


@celery.task
def send_about(activity):
    print('>> inside send_about')
    # credentials = MicrosoftAppCredentials(APP_ID, APP_PASSWORD)
    # connector = ConnectorClient(credentials, base_url=activity.service_url)
    reply = __create_reply_activity(activity, "You said: %s" % activity.text)
    # connector.conversations.send_to_conversation(reply.conversation.id, reply)

    connector.conversations.send_to_conversation(reply.conversation.id, reply)
    reply, url = __create_reply_activity(activity, "HERE!!")
    res = connector.push(url, reply)
    # return json.dumps({'status': res.status_code, 'text': res.text})

#
# @celery.task
# def record_user(activity):
#     uid = activity['from']['id'] or ''
#     if not uid:
#         raise Exception('User id not found:\n' + json.dumps(activity))
#     activity['from'], activity['recipient'] = activity['recipient'], activity[
#         'from']
#     user.save(uid, activity)
#
#
# @celery.task
# def send_help(activity):
#     help_msg = bot.get_help_msg() or 'Try to enter /cat command first.'
#     reply, url = __create_reply_activity(activity, help_msg)
#     connector.push(url, reply)
#
#     return 'help', activity['from']['id']
#
#
# @celery.task
# def user_subscribe(activity):
#     uid = activity['from']['id']
#     is_sub = user.is_subscribe(uid)
#
#     if is_sub:
#         push_msg = bot.get_already_sub_msg(
#         ) or 'Already subscribe, enter /unsub to cancel it.'
#     else:
#         user.add_subscribe(uid)
#         push_msg = bot.get_sub_msg(
#         ) or 'Subscribe success! enter /unsub to cancel it.'
#
#     reply, url = __create_reply_activity(activity, push_msg)
#     connector.push(url, reply)
#
#     return ('subscribe', uid)
#
#
# @celery.task
# def user_unsubscribe(activity):
#     uid = activity['from']['id']
#     is_sub = user.is_subscribe(uid)  # for #25
#     if is_sub:
#         user.rm_subscribe(uid)
#
#     push_msg = bot.get_unsub_msg(
#     ) or 'Unsubscribe success! enter /sub to get more cats everyday.'
#
#     reply, url = __create_reply_activity(activity, push_msg)
#     connector.push(url, reply)
#
#     return ('unsubscribe', uid)
#
#
# @celery.task
# def push():
#     if holiday.is_holiday():
#         return ('push stop', 'is holiday')
#     cats = cat.get_list()
#     for uid in user.get_subscribes():
#         try:
#             ig_account = cat.get_uid(choice(cats))
#             activity = user.get(uid)
#             url = '{}/v3/conversations/{}/activities'.format(
#                 activity['serviceUrl'], activity['conversation']['id'])
#             push_msg = bot.get_push_msg() or ''
#             activity['text'] = push_msg + __ig_host__.format(ig_account)
#             connector.push(url, activity)
#         except:
#             logging.error('FAILURE: push msg to user {}'.format(uid))
#     return 'push'
#
#
# @celery.task
# def push_cat(activity):
#     uid = activity['from']['id']
#     reply, url = __create_reply_activity(activity)
#
#     is_sub = user.is_subscribe(uid)
#     if not is_sub:
#         ask_msg = bot.get_ask_sub_msg()
#         reply['text'] = ask_msg or 'See more cats everyday use /sub command.'
#         connector.push(url, reply)
#
#     cats = cat.get_list()
#     ig_account = choice(cats).split(':')[1]
#     push_msg = bot.get_push_msg() or ''
#     reply['text'] = push_msg + __ig_host__.format(ig_account)
#     connector.push(url, reply)
#     return (uid, ig_account)
