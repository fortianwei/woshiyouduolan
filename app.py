__author__ = 'tianwei'
import os.path
import pymongo
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpserver
from tornado.options import define,options
from tornado.web import url

from handlers import handlers
define("port", default=2333, type=int)
define("config_file", default="app_config.yml", help="app_config file")

MONGO_SERVER = "localhost"


class Application(tornado.web.Application):
    def __init__(self, **overrides):
        handler = [
            url(r'/', handlers.WelcomeHandler, name='index'),
            url(r'/post', handlers.PostHandler, name='post'),
            url(r'/article/([a-z]+)/([0-9]+)', handlers.ArticledHandler, name='article'),

            url(r'/bower_components/(.*)', tornado.web.StaticFileHandler, {'path': 'bower_components'}),
            url(r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'})



        ]

        settings = {
            'template_path':os.path.join(os.path.dirname(__file__), 'static/html/')
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