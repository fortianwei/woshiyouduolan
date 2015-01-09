from tornado.web import RequestHandler
from datetime import datetime

class BaseHandler(RequestHandler):

    @property
    def db(self):
        return self.application.syncdb


class WelcomeHandler(BaseHandler):
    def get(self):
        collection_articles = self.db.articles
        articles = collection_articles.find()
        articles2 = collection_articles.find()
        self.render('index.html', articles=articles, articles2=articles2)


class PostHandler(BaseHandler):
    def get(self):
        self.render('post.html')

    def post(self, *args, **kwargs):
        title = self.get_body_argument('title', default='No title')
        content = self.get_body_argument('content', default='No content')
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        articles = self.db.articles
        article = {'title': title, 'content': content, 'time': time}

        articles.insert(article)
        print self.get_body_argument('title')
        print self.get_body_argument('content')
        print time


class ArticledHandler(BaseHandler):
    def get(self, article_id):
        print article_id


        article = self.db.articles.find_one({'id': int(article_id)})
        print article['content']
        # article['content'] = article['content'].replace('<pre>', '\n    ')
        import markdown
        article['content'] = markdown.markdown(article['content'], extensions=['markdown.extensions.codehilite']) #highlight(article['content'], lexer, formatter)
        print article['content']
        self.render('article.html',article=article)