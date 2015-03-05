# coding=utf-8
from base import BaseHandler
import pymongo


class WelcomeHandler(BaseHandler):

    def get(self):
        collection_articles = self.db.articles
        articles = collection_articles.find().sort('time', pymongo.DESCENDING)
        articles2 = collection_articles.find().sort('time', pymongo.DESCENDING).limit(10)
        self.render('index.html', articles=articles, articles2=articles2)
