import json
import datetime
import webapp2

__author__ = 'kenneth'


class PregnancyDate(webapp2.RequestHandler):
    def get(self):
        weeks = self.request.get('weeks', 0)
        self.response.headers['content-type'] = 'application/json'
        if weeks.isdigit():
            days = int(weeks) * 7
            p_date = datetime.datetime.today() - datetime.timedelta(days=days)
            preg_date = p_date.strftime("%a, %d %b %Y %H:%M:%S GMT")
            self.response.write(json.dumps(dict(valid='true', preg_date=preg_date)))
        else:
            self.response.write(json.dumps({'valid': "false"}))