from tornado.web import RequestHandler
from datetime import datetime

class BaseHandler(RequestHandler):

    @property
    def db(self):
        return self.application.syncdb


class WelcomeHandler(BaseHandler):
    def get(self):
        print 1111
        self.render('index.html')


class PostHandler(BaseHandler):
    def get(self):
        self.render('post.html')

    def post(self, *args, **kwargs):
        title = self.get_body_argument('title', default='No title')
        content = self.get_body_argument('content', default='No content')
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        articles = self.db.articles
        article ={'title':title,'content':content,'time':time}

        articles.insert(article)
        print self.get_body_argument('title')
        print self.get_body_argument('content')
        print time