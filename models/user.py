# encoding = utf-8


class User(object):

    def __init__(self, uid, name, password, user_info_id):
        self.uid = uid
        self.name = name
        self.password = password
        self.user_info_id = user_info_id