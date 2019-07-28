# -*- coding: utf-8 -*-
from app.bot import handlers
from app.common.exceptions import UnhandledException

__activity_conversation_update__ = 'conversationUpdate'
__activity_message__ = 'message'


def __msg_processor__(msg):
    # handlers.record_user.delay(msg)

    command = msg['text'].split(' ')[0]
    if command == '你是誰' or command == '/about':
        print('heyhey')
        handlers.send_about.delay(msg)
    # elif command == '/sub':
    #     handlers.user_subscribe.delay(msg)
    # elif command == '/unsub':
    #     handlers.user_unsubscribe.delay(msg)
    # elif command == '/cat':
    #     handlers.push_cat.delay(msg)
    # else:
    #     handlers.send_help.delay(msg)


def adapter(msg):
    msg_type = msg['type'] or ''
    if msg_type == __activity_conversation_update__:
        pass
    elif msg_type == __activity_message__:
        __msg_processor__(msg)
    else:
        raise UnhandledException()
