# run this file the first time to setup ids table
from pymongo import Connection

conn = Connection()
db = conn.vs
if db.ids.count() == 0:
    db.ids.insert({"tablename": "articles", "id": 1})
    import hashlib
    import base64
    password = 'yourpassword'
    hash = hashlib.md5()
    hash.update(password)
    value = hash.digest()
    db.users.insert({'username': 'tianwei', 'password': base64.encodestring(value).replace('\n', '')})
    print "Setup success"
else:
    print "Has been initialized before,ignore this time."
