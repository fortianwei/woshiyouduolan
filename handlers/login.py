# coding=utf-8

from base import BaseHandler
import utils

from tornado import gen

class LoginHandler(BaseHandler):
    def get(self):
        next_page = self.get_argument('next', '/')
        self.render("login.html", next=next_page)

    @gen.coroutine
    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')
        password = utils.getBase64EncodedMD5String(password)
        print username, password
        user = self.db.users.find({'username': username, 'password': password})
        count = yield user.count()
        if count > 0:
            print 'Check user success.'
            self.set_secure_cookie('current_user', unicode(username))
            print 'next is ', self.get_argument("next", "/")
            self.redirect(self.get_argument("next", "/"))
        else:
            print 'Check user failed.'
            self.redirect('/')
