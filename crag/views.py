import json
import urllib
from google.appengine.api import urlfetch
import webapp2


__author__ = 'kenneth'


class MakeCallRequestHandler(webapp2.RequestHandler):

    def get(self):
        VOICE_URL = "http://voice.tmcg.co.ug/hiwa-calls/index.php?r=tocall/create"
        phone = self.request.get('phone').replace(" ", "")
        code = "mcrag/%s" % self.request.get('code')
        post_data = "Tocall[number]=%s&Tocall[class]=%s" % (phone, code)
        result = urlfetch.fetch(url=VOICE_URL, payload=post_data, method=urlfetch.POST,
                                headers={'Content-Type': 'application/x-www-form-urlencoded'})
        if 199 < result.status_code < 300:
            self.response.write(json.dumps({"success": True}))
        else:
            self.response.write(json.dumps({"success": False, "code": result.status_code}))