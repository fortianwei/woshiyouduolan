# coding = utf-8


class UserInfo(object):

    def __init__(self, nickname, pic, **kwargs):
        self.nickname = nickname
        self.pic = pic
        self.other_infos = kwargs