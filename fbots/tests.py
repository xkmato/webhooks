from unittest import TestCase
from models import User

__author__ = 'kenneth'


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User(phone='0799444444', fb_id='09402934343')
        self.user.put()

    def test_get_by_fb_id(self):
        self.assertEquals(User.get_by_fb_id('09402934343'), self.user)

    def test_get_by_phone(self):
        self.assertEquals(User.get_by_phone('0799444444'), self.user)

    def test_get_or_create(self):
        self.assertEquals(User.query().count(), 1)
        User.get_or_create("UNKNOWN USER")
        self.assertEquals(User.query().count(), 2)
        User.get_or_create("UNKNOWN USER")
        self.assertEquals(User.query().count(), 2)