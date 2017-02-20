# coding=utf-8

from base import BaseHandler
from tornado import gen
class TimelineHandler(BaseHandler):

    @gen.coroutine
    def get(self):

        timelines = self.db.timelines
        pp = yield timelines.find().to_list(10000)
        self.render('timeline.html', pp=pp)

    def post(self):
        pass