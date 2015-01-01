__author__ = 'tianwei'
from tornado.web import RequestHandler

class BaseHandler(RequestHandler):

    @property
    def db(self):
        return self.application.syncdb


class WelcomeHandler(BaseHandler):
    def get(self):
        print 1111
        self.render('index.html')

class PostHandler(BaseHandler):
    def get(self):
        self.render('post.html')