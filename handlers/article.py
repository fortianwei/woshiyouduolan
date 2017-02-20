# coding=utf-8
from base import BaseHandler
import tornado.web
import tornado.gen


class ArticleHandler(BaseHandler):

    @tornado.gen.coroutine
    def get(self, article_id, operation):
        # print article_id, operation

        article = yield self.db.articles.find_one({'id': int(article_id)})

        if not article:
            raise tornado.web.HTTPError(404)
        else:
            article['id'] = int(article_id)
            if 'tags' not in article:
                article['tags'] = ''
            #article['visit_count'] = 1 if not article.has_key('visit_count') else article['visit_count'] + 1
            #self.db.articles.update({'id': article['id']}, {'$set': article}, True)
            # print 'here ',article['visit_count']
            yield self.db.articles.find_and_modify({'id': article['id']}, update={"$inc": {"visit_count": 1}}, upsert=True)
        if operation is None:
            #print type(article['content'])
            #print article['content'].decode('utf-8')
            # article['content'] = article['content'].replace('<pre>', '\n    ')
            # article['content'] = article['content'].replace('</pre>', '')
            #import markdown
            import markdown2
            # article['content'] = markdown.markdown(article['content'], extensions=['markdown.extensions.codehilite']) #highlight(article['content'], lexer, formatter)
            article['content'] = markdown2.markdown(article['content'], extras=['fenced-code-blocks'])
            #print article['content'].decode('utf-8')

            self.render('article.html', article=article)

        if operation == '/edit':
            article['tags'] = ','.join(article['tags'])
            if self.get_secure_cookie('current_user') is not None:
                self.render('edit.html', article=article)
            else:
                self.redirect('/login')
