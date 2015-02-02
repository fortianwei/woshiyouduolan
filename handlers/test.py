# from pymongo import Connection
# import hashlib
# import base64
# conn = Connection()
# db = conn.vs
# password = 'xxxx'
# hash = hashlib.md5()
# hash.update(password)
# value = hash.digest()
# db.users.insert({'username': 'tianwei', 'password': base64.encodestring(value).replace('\n', '')})
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


l=[33,2,45,23,555,233,14,67,856]

def quick_sort(l,low,high):
    if low > high:
        return

    pivot = l[low]
    i = low
    j = high

    while i<j:
        while i<j and l[j] >= pivot:
            j-=1
        l[i] = l[j]
        while i<j and l[i] < pivot:
            i+=1
        l[j] = l[i]
        l[i] = pivot

    quick_sort(l, low, i-1)
    quick_sort(l, i+1,high)

quick_sort(l,0,len(l)-1)
print l

#binary search
def find(l, low, high, n):

    while low <= high:

        mid = (low+high)/2
        if l[mid] == n:
            return mid

        if l[mid] < n:
            low = mid + 1
        if l[mid] > n:
            high = mid - 1
    return -1

print find(l,0,len(l)-1,555)