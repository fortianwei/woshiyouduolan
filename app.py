__author__ = 'tianwei'
import os.path
import pymongo
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpserver
from tornado.options import define,options
from tornado.web import url

from handlers import *
define("port", default=2333, type=int)
define("config_file", default="app_config.yml", help="app_config file")

MONGO_SERVER = "localhost"


class Application(tornado.web.Application):
    def __init__(self, **overrides):
        handler = [
            url(r'/', welcome.WelcomeHandler, name='index'),
            url(r'/index\.html', welcome.WelcomeHandler, name='index'),
            url(r'/login', login.LoginHandler, name='login'),
            url(r'/post/?([0-9]+)?', post.PostHandler, name='post'),
            url(r'/article/([0-9]+\.?[0-9]*)(/[a-z]+)?', article.ArticledHandler, name='article'),

            url(r'/bower_components/(.*)', tornado.web.StaticFileHandler, {'path': 'bower_components'}),
            url(r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
            url(r'.*', file_not_found.FileNotFoundHandler, name='404')


        ]

        settings = {
            'template_path': os.path.join(os.path.dirname(__file__), 'static/html/'),
            'login_url': '/login',
            'cookie_secret': '&&*#@DFjjjs11f=3(((gd000d\dfasd@)'
        }

        tornado.web.Application.__init__(self, handler, **settings)
        self.syncConnection = pymongo.Connection(MONGO_SERVER, 27017)

        if 'db' in overrides:
            self.syncdb = self.syncConnection[overrides['db']]
        else:
            self.syncdb = self.syncConnection['vs']


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    print options.port

    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()