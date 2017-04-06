import json
from google.appengine.api import urlfetch
import settings

__author__ = 'kenneth'


def is_valid_phone(number):
    if len(number) == 10 and str(number).isdigit():
        return True
    return False


def is_initial_command(user, text):
    if not user.get_open_orders().get() and text.lower() in settings.INITIAL_COMMANDS:
        return True
    return False


def post_menu(menu):
        post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s' % settings.FB_ACCESS_TOKEN
        return urlfetch.Fetch(post_message_url, method=urlfetch.POST, headers={"Content-Type": "application/json"},
                              payload=json.dumps(menu))