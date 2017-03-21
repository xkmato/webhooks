import json
import webapp2
from smsmaama.utils import get_preg_date

__author__ = 'kenneth'


class PregnancyDate(webapp2.RequestHandler):
    def get(self):
        weeks = self.request.get('weeks', 0)
        self.response.headers['content-type'] = 'application/json'
        if weeks.isdigit():
            preg_date = get_preg_date(weeks)
            self.response.write(json.dumps(dict(valid='true', preg_date=preg_date)))
        else:
            self.response.write(json.dumps({'valid': "false"}))