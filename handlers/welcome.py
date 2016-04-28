# coding=utf-8
from base import BaseHandler
import pymongo
import tornado.gen


class WelcomeHandler(BaseHandler):

    def __init__(self, application, request, **kwargs):
        super(WelcomeHandler, self).__init__(self, application, request, kwargs)
        self.page_size = 6
        self.side_articles_num = 8

    @tornado.gen.coroutine
    def get(self, page):
        page = int(page) if page else 1
        print 'page is ', page
        collection_articles = self.db.articles
        # 分页
        cursor = collection_articles.find().sort('time', pymongo.DESCENDING).\
            skip(self.page_size * (page - 1)).limit(self.page_size)
        cursor2 = collection_articles.find().sort('time', pymongo.DESCENDING).limit(self.side_articles_num)
        articles = yield cursor.to_list(length=self.page_size)
        articles2 = yield cursor2.to_list(length=self.side_articles_num)
        count = yield collection_articles.count()
        self.render('index.html', articles=articles, articles2=articles2, count=int(count/self.page_size) +
                                                                                (1 if count % self.page_size != 0 else 0))
