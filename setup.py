# run this file the first time to setup ids table
from pymongo import Connection
from handlers import utils

conn = Connection()
db = conn.vs
if db.ids.count() == 0:
    db.ids.insert({"tablename": "articles", "id": 1})
    password = 'yourpassword'
    db.users.insert({'username': 'tianwei', 'password': utils.getBase64EncodedMD5String(password)})
    print "Setup success"
else:
    print "Has been initialized before,ignore this time."
