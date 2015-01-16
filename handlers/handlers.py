import pymongo
import tornado.web
from tornado.web import RequestHandler
from datetime import datetime

class BaseHandler(RequestHandler):

    @property
    def db(self):
        return self.application.syncdb

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('404.html')

class WelcomeHandler(BaseHandler):
    def get(self):
        collection_articles = self.db.articles
        articles = collection_articles.find().sort('time', pymongo.DESCENDING)
        articles2 = collection_articles.find().sort('time', pymongo.DESCENDING)
        self.render('index.html', articles=articles, articles2=articles2)


class PostHandler(BaseHandler):
    def get(self, article_id):
        self.render('post.html')

    def post(self, article_id):
        print 'article_id:', article_id

        title = self.get_body_argument('title', default='No title')
        content = self.get_body_argument('content', default='No content')
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        articles = self.db.articles
        article = {'title': title, 'content': content, 'time': time}

        article['id'] = article_id
        if article_id is None:
            ret = self.db.ids.find_and_modify({'tablename': "articles"}, update={"$inc": {"id": 1}}, new=True)
            article['id'] = ret['id']
            print "new id:", article['id']

        articles.update({'id': article['id']}, article, True)
        self.redirect('/')
        print self.get_body_argument('title')
        print self.get_body_argument('content')
        print time


class ArticledHandler(BaseHandler):
    def get(self, operation, article_id):
        print operation, article_id

        article = self.db.articles.find_one({'id': int(float(article_id))})
        if not article:
            raise tornado.web.HTTPError(404)
        if operation is None:
            print article['content']
            # article['content'] = article['content'].replace('<pre>', '\n    ')
            import markdown
            article['content'] = markdown.markdown(article['content'], extensions=['markdown.extensions.codehilite']) #highlight(article['content'], lexer, formatter)
            print article['content']
            self.render('article.html', article=article)

        if operation == '/edit':
            self.render('edit.html', article=article)