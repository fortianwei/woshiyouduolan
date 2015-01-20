# run this file the first time to setup ids table
from pymongo import Connection

conn = Connection()
db = conn.vs
if db.ids.count() == 0:
    db.ids.insert({"tablename": "articles", "id": 1})
    print "Setup success"
else:
    print "Has been initialized before,ignore this time."
