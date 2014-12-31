__author__ = 'tianwei'
from tornado.web import RequestHandler

class BaseHandler(RequestHandler):

    @property
    def db(self):
        return self.application.syncdb


class WelcomeHandler(BaseHandler):
    def get(self):
        print 1111
        self.render('index.html')



users = db.users

user = {"name": "tianwei", "age": "33"}
users.insert(user)


# print users.find_one()

# xx = users.find({"name":"tianwei"})
xx = users.find()
for x in xx:
    print x
print xx.count()
# del xx["_id"]
# yy = json.dumps(xx)
# print yy