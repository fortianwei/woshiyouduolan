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
        img = self.get_body_argument('img', default='')
        tags = map(lambda x: x.strip(), tags)
        pp = self.get_body_argument('kuso', 'no')
        print 'pp is ', pp
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data_set = {'title': title, 'content': content, 'modify_time': now}
        # article = {'title': title, 'content': content, 'modify_time': time, 'tags': tags}
        if pp == 'on':
            # timeline
            data_set['img'] = img
            table_name = 'timelines'
        else:
            data_set['tags'] = tags
            table_name = 'articles'

        if article_id is None:
            ret = yield self.db.ids.find_and_modify({'tablename': table_name}, update={"$inc": {"id": 1}}, new=True)
            article_id = ret['id']
            data_set['time'] = now
            data_set['visit_count'] = 0
        else:
            # timeline does not support edit
            article_id = int(float(article_id))
        data_set['id'] = article_id

        yield self.db[table_name].update({'id': article_id}, {'$set': data_set}, True)
        self.redirect('/')
