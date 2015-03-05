# coding=utf-8

from base import BaseHandler
import utils


class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')
        password = utils.getBase64EncodedMD5String(password)
        print username, password
        user = self.db.users.find({'username': username,'password': password})
        if user.count() > 0:
            print 'Check user success.'
            self.set_secure_cookie('current_user', unicode(username))
            self.redirect(self.get_argument("next", "/"))
        else:
            print 'Check user failed.'
            pass