# coding=utf-8
import tornado.web
import tornado.gen
from base import BaseHandler
from datetime import datetime


class PostHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, article_id):
        self.render('post.html')

    '''
    /post:post a new article
    /post/id : modify article with its id
    '''
    @tornado.gen.coroutine
    @tornado.web.authenticated
    def post(self, article_id):
        print 'article_id:', article_id

        title = self.get_body_argument('title', default='No title')
        content = self.get_body_argument('content', default='No content')
        tags = self.get_body_argument('tags', default='').split(',')
        tags = map(lambda x: x.strip(), tags)
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        article = {'title': title, 'content': content, 'time': time, 'modify_time': time, "tags": tags}

        set_data = {'title': title, 'content': content, 'modify_time': time, 'tags': tags}

        if article_id is None:
            ret = yield self.db.ids.find_and_modify({'tablename': "articles"}, update={"$inc": {"id": 1}}, new=True)
            article['id'] = ret['id']
            set_data['time'] = time
            set_data['visit_count'] = 0
            print "new id:", article['id']
        else:
            article['id'] = int(float(article_id))
        set_data['id'] = article['id']

        yield self.db.articles.update({'id': article['id']}, {'$set': set_data}, True)
        self.redirect('/')
        #print self.get_body_argument('title')
        #print self.get_body_argument('content')
        #print time
