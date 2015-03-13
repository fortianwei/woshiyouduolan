# coding=utf-8
from base import BaseHandler


class TryJs(BaseHandler):
    def get(self):
        self.render("/try_js.html")

    def post(self):
        content = self.get_body_argument("textareaCode")
        print content

class TryJsCode(BaseHandler):
    def get(self):
        pass
