# coding=utf-8

from tornado.web import RequestHandler
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class BaseHandler(RequestHandler):

    @property
    def db(self):
        return self.application.asyncdb

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('404.html')

    def get_current_user(self):
        print 'get_current_user ', self.get_secure_cookie('current_user')
        return self.get_secure_cookie('current_user')

