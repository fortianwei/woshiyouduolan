# coding=utf-8
from base import BaseHandler
import pymongo
import tornado.gen


class WelcomeHandler(BaseHandler):

    @tornado.gen.coroutine
    def get(self, page):
        page = int(page) if page else 1
        print 'page is ', page
        collection_articles = self.db.articles
        # 分页
        cursor = collection_articles.find().sort('time', pymongo.DESCENDING).skip(10 * (page - 1)).limit(10)
        cursor2 = collection_articles.find().sort('time', pymongo.DESCENDING).limit(8)
        articles = yield cursor.to_list(length=10)
        articles2 = yield cursor2.to_list(length=8)
        count = yield collection_articles.count()
        self.render('index.html', articles=articles, articles2=articles2, count=int(count/10) +
                                                                                (1 if count % 10 != 0 else 0))
