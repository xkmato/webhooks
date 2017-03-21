from unittest import TestCase
import datetime
from smsmaama.utils import get_preg_date

__author__ = 'kenneth'


class UtilsTestCase(TestCase):
    def test_get_preg_date(self):
        days = 1 * 7
        p_date = datetime.datetime.today() - datetime.timedelta(days=days)
        self.assertEquals(get_preg_date(1), p_date.strftime("%a, %d %b %Y %H:%M:%S GMT"))