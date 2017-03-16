import webapp2

__author__ = 'kenneth'


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
