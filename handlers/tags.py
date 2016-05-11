# coding=utf-8
from base import BaseHandler
import pymongo
import tornado.gen

class TagsHandler(BaseHandler):

    @tornado.gen.coroutine
    def get(self, tag):
        collection_articles = self.db.articles
        # 分页
        cursor = collection_articles.find({'tags': tag}).sort('time', pymongo.DESCENDING)
        articles = yield cursor.to_list(1000)
        self.render('tags.html', articles=articles)

