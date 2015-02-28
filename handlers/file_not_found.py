# coding=utf-8
from base import BaseHandler

class FileNotFoundHandler(BaseHandler):
    def get(self):
        self.render('404.html')
