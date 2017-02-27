# coding=utf-8

from base import BaseHandler
from tornado import gen
from collections import OrderedDict


class TimelineHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        timelines = self.db.timelines
        pp = yield timelines.find().sort('time', -1).to_list(10000)
        new_pp = OrderedDict()
        for timeline in pp:
            time_day = timeline['time'][:10]
            if time_day in new_pp:
                new_pp[time_day].append(timeline)
            else:
                new_pp[time_day] = [timeline]

        self.render('timeline.html', pp=new_pp)

    def post(self):
        pass
