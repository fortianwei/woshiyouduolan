from pymongo import Connection
import hashlib
import base64
conn = Connection()
db = conn.vs
password = 'xxxx'
hash = hashlib.md5()
hash.update(password)
value = hash.digest()
db.users.insert({'username': 'tianwei', 'password': base64.encodestring(value).replace('\n', '')})
#print base64.encodestring(value).replace('\n', '')
# count = 1
# article = db.articles.find_one({'id': 1})
# idd = db.ids.find_and_modify(query={'tablename': 'articles'}, update={"$set": {"id": 10}}, new=True)
# print idd["id"]
# print article
#
# def xx():
#         import mistune
#         from pygments import highlight
#         from pygments.lexers import get_lexer_by_name
#         from pygments.formatters.html import HtmlFormatter
#
#         class MyRenderer(mistune.Renderer):
#             def block_code(self, code, lang='python'):
#                 print 11122222222222
#                 if not lang:
#                     return '\n<pre><code>%s</code></pre>\n' % mistune.escape(code)
#                 lexer = get_lexer_by_name(lang, stripall=True)
#                 formatter = HtmlFormatter()
#                 return highlight(code, lexer, formatter)
#
#
#
#
#         article = {}
#         article['content'] = 'I am using **markdown** <pre><code>print 123</code></pre>'
#         md = mistune.Markdown(renderer=MyRenderer())
#         print article['content']
#         article['content'] = md.render(article['content'])
#         print article['content']
#         code = 'wocao***dd** <pre><code>print "Hello World"</code></pre>'
#         lexer = get_lexer_by_name('python', stripall=True)
#         print highlight(code, lexer, HtmlFormatter())
#
#         import markdown
#         ret = markdown.markdown(code, ['codehilite'])
#         print ret
#
#


#
# import markdown
# ss = markdown.markdown(r"```python\nprint 111\n```",extensions=['markdown.extensions.codehilite'])
# print ss
#
# import markdown2
# bb = markdown2.markdown("```python\nprint 111\n```", extras=['fenced-code-blocks'])
# print bb