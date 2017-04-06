import logging
from models import UI, User
from utils import post_menu, is_valid_phone, is_initial_command
import settings


def handle_postback(user, message):
    order = None
    if message == settings.GET_STARTED_BUTTON_PAYLOAD or is_initial_command(user, message):
        post_menu(UI.create_main_menu(user))
    elif message.startswith(settings.START_OVER_PAYLOAD):
        user.close_open_boarders()
        post_menu(UI.create_main_menu(user))
    elif message.startswith(settings.MAIN_ORDER_PAYLOAD_PREFIX):
        post_menu(UI.create_extra_menu(user))
    elif message.startswith(settings.EXTRA_ORDER_PAYLOAD_PREFIX):
        post_menu(UI.create_order_status(order))
    elif message == settings.SKIP_EXTRA_PAYLOAD:
        post_menu(UI.create_order_status(order))
    elif message == settings.CANCEL_ORDER_PAYLOAD:
        post_menu(UI.create_order_status(settings.ORDER_CANCELED_TEXT))


def start_handling(incoming_message):
    for entry in incoming_message['entry']:
        for message in entry['messaging']:
            msg = ""
            sender = message['sender']['id']
            user = User.get_or_create(sender)
            if "postback" in message:
                msg = message['postback']['payload']
            elif "message" in message:
                msg = message["message"]["text"]
                if 'quick_reply' in message["message"]:
                    msg = message["message"]['quick_reply']['payload']
            logging.info(message)
            handle_postback(user, msg)