class test1(object):

    @classmethod
    def aaaab(clazz):
        wori = 3
        print 111

    @staticmethod
    def aaaa():
        wori = 3
        print 222
    dd = 3

    def __init__(self):
        self.name = 11
        self.age = 33

    def listall(self):
        for name,value in vars(self).items():
            print name,value


class Wori(test1):
    def __init__(self):
        super(Wori, self).__init__()
        self.bbbb = 3

aa = Wori()
aa.listall()
aa.aaaa()
aa.aaaab()
Wori.aaaa()
Wori.aaaab()
