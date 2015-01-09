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

from pymongo import Connection

conn = Connection()
db = conn.vs
count = 1
article = db.articles.find_one({'id': 1})
print article

def xx():
        import mistune
        from pygments import highlight
        from pygments.lexers import get_lexer_by_name
        from pygments.formatters.html import HtmlFormatter

        class MyRenderer(mistune.Renderer):
            def block_code(self, code, lang='python'):
                print 11122222222222
                if not lang:
                    return '\n<pre><code>%s</code></pre>\n' % mistune.escape(code)
                lexer = get_lexer_by_name(lang, stripall=True)
                formatter = HtmlFormatter()
                return highlight(code, lexer, formatter)




        article = {}
        article['content'] = 'I am using **markdown** <pre><code>print 123</code></pre>'
        md = mistune.Markdown(renderer=MyRenderer())
        print article['content']
        article['content'] = md.render(article['content'])
        print article['content']
        code = 'wocao***dd** <pre><code>print "Hello World"</code></pre>'
        lexer = get_lexer_by_name('python', stripall=True)
        print highlight(code, lexer, HtmlFormatter())

        import markdown
        ret = markdown.markdown(code, ['codehilite'])
        print ret


import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter


class MyRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        print "ccccccccccc"
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)

renderer = MyRenderer()
md = mistune.Markdown(renderer=renderer)
print(md.render(r'Some Markdown text.'
                r'    print 123'))

import markdown
ss = markdown.markdown(r"    print 111",extensions=['markdown.extensions.codehilite'])
print ss

import markdown2
bb = markdown2.markdown("<pre>print 111</pre>", extras=[ 'fenced-code-blocks'])
print bb