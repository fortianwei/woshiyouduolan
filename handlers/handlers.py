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


class FileNotFoundHandler(BaseHandler):
    def get(self):
        self.render('404.html')



class PostHandler(BaseHandler):
    def get(self, article_id):
        self.render('post.html')

    '''
    /post:post a new article
    /post/id : modify article with its id
    '''
    def post(self, article_id):
        print 'article_id:', article_id

        title = self.get_body_argument('title', default='No title')
        content = self.get_body_argument('content', default='No content')
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        articles = self.db.articles
        article = {'title': title, 'content': content, 'time': time, 'modify_time': time}

        set_data = {'title': article['title'], 'content': article['content'], 'modify_time': article['modify_time']}

        if article_id is None:
            ret = self.db.ids.find_and_modify({'tablename': "articles"}, update={"$inc": {"id": 1}}, new=True)
            article['id'] = ret['id']
            article['time'] = time
            print "new id:", article['id']
        else:
            article['id'] = int(float(article_id))
        set_data['id'] = article['id']

        articles.update({'id': article['id']}, {'$set': set_data}, True)
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
        else:
            article['id'] = int(float(article_id))

        if operation is None:
            print article['content']
            # article['content'] = article['content'].replace('<pre>', '\n    ')
            # article['content'] = article['content'].replace('</pre>', '')
            import markdown
            import markdown2
            # article['content'] = markdown.markdown(article['content'], extensions=['markdown.extensions.codehilite']) #highlight(article['content'], lexer, formatter)
            article['content'] = markdown2.markdown(article['content'], extras=['fenced-code-blocks'])
            print article['content']

            self.render('article.html', article=article)

        if operation == '/edit':
            self.render('edit.html', article=article)