from google.appengine.ext import ndb
import settings
from utils import is_valid_phone

__author__ = 'kenneth'


class UI(object):
    @staticmethod
    def create_menu(user, menu):
        menu = dict(recipient=dict(id=user.fb_id), message=menu)
        return menu

    @staticmethod
    def create_main_menu(user):
        return UI.create_menu(user, Product.to_main_menu())


    @classmethod
    def create_order_status(cls, order, message=None):
        return cls.create_menu(order.user.get(), order.to_response(message=message))


class BaseModel(ndb.Model):
    created_on = ndb.DateTimeProperty(auto_now_add=True)
    modified_on = ndb.DateTimeProperty(auto_now=True)


class User(BaseModel):
    phone = ndb.StringProperty()
    fb_id = ndb.StringProperty()

    def process_message(self, message):
        if is_valid_phone(message):
            self.phone = message
            self.put()
            return
        return settings.ORDER_PHONE_VALIDATION_FAIL

    @classmethod
    def get_by_fb_id(cls, fb_id):
        return cls.query().filter(cls.fb_id == fb_id).get()

    @classmethod
    def get_by_phone(cls, phone):
        return cls.query().filter(cls.phone == phone).get()

    @classmethod
    def get_or_create(cls, fb_id):
        user = cls.get_by_fb_id(fb_id)
        if not user:
            user = cls(fb_id=fb_id)
            user.put()
        return user


class Product(ndb.Model):
    @classmethod
    def to_main_menu(cls):
        pass