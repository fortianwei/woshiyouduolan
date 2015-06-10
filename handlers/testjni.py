from base import BaseHandler
from datetime import datetime
class TestJniHandler(BaseHandler):
    def get(self):
        prop = self.get_query_argument("prop", default = "default")
        sha1 = self.get_query_argument("sha1", default = "default")
        imei = self.get_query_argument("imei", default = "default")
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print 'testjni here,prop = ', prop, 'sha1 = ', sha1, 'imei' , imei
        testjni = self.db.testjni
        data = {'time': time, 'prop': prop, 'sha1': sha1, 'imei' : imei}
        ret = self.db.ids.find_and_modify({'tablename' : 'testjni'}, update = {'$inc' : {'id' : 1}},new = True)
        id = ret['id']
        testjni.update({'id' : id },{'$set' : data}, True)
        self.write("success")
    
    def post(self):
        self.get()
