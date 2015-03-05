# coding=utf-8

from base import BaseHandler

class CommentsHandler(BaseHandler):

    def get(self):
        self.render('comments.html')

    def post(self):
        pass