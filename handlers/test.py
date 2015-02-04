#coding=utf-8

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

#project euler 4　
#求由两个三位数相乘得到的最大的回文数(9009是两个两位数相乘得到的最大回文数,9009=99*91)
# l=[]
# for i in range(1,999):
#     for j in range (1,999):
#         if str(i*j) == str(i*j)[::-1]:
#             l.append(i*j)
#
# l.sort(reverse=True)
# print l[0]

#project euler 5
#最小公倍数　＝m*n/最大公约数
#求1到20的最小公倍数
#最大公约数：欧几里德算法
# def gcd(m, n):
#     while n:
#         m, n = n, m % n
#     return m
#
# print reduce(lambda a, x: a*x/gcd(a, x), range(1, 21))
i=3

#project euler 6
#求1到100的和的乘积　－　乘积的和
#pow（(１＋２＋３＋．．．＋１００),2） - (pow(1,2)+sqrt(2,2)+...+sqrt(100,2))
from math import pow
print pow(sum(list(range(1,101))),2) - sum([pow(i,2) for i in(range(1,101))])

#project euler 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
# from math import  sqrt
# def checkPrime(m):
#     nn = int(sqrt(m))
#     for i in range(2,nn+1):
#         if m%i == 0:
#             return False
#     return True
# n=0
# import itertools
# for i in itertools.count(2):
#     if checkPrime(i):
#         n+=1
#         print 'n＝',n,' i=',i
#         if n==10001:
#             break;

#直接for　range　太占内存,用itertools.count创建迭代器好点

#project euler 7
#找出给出１０００个数中连续的１３个数，这１３个数的乘积最大

l = '''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''
# l = l.replace('\n','')
# #思路,不要挨个算乘积,应该是找出那些有0的数,略过一些步骤,再去乘
# print sorted(map(lambda s: reduce(lambda a, m: a*int(m),list(s), 1),
#              [l[i:i+13] for i in range(0, 988)]), reverse=True)[0]

#project euler 9
#a+b+c=1000  pow(a,2)+pow(b,2)=pow(c,2),勾股定理,求a*b*c
#先手动计算 a = (500000-1000*b)/(1000-b),a设定为最小值,那么a范围不大于1000/(2+sqrt(2))
#这样就只需要遍历一次1~1000而不是a,b,c都遍历1~1000
# from math import pow, sqrt
# import time
# start = time.clock()
# a = filter(lambda x: x**2+pow((500000-1000*x)/(1000-x),2) == pow(1000-x-(500000-1000*x)/(1000-x),2),xrange(1,int(1000/(2+sqrt(2)))))[0]
# print a*((500000-1000*a)/(1000-a))*(1000-a-(500000-1000*a)/(1000-a))
# print 'time used:',time.clock() - start

#project euler 10
#质数累加,2000000以内的质数累加
# def checkPrime(m):
#     nn = int(m**0.5)
#     for i in range(2,nn+1):
#         if m%i == 0:
#             return False
#     return True
#
# print sum(filter(lambda x:checkPrime(x),range(2,2000000)))

#上面是死办法,速度很慢还有一种,找质数法
#就是从2开始,去掉其所有倍数,3没有被去掉,那么再去掉3的所有倍数,然后是5
#一直到n**0.5(也就是sqrt(n)),剩下没有被去掉的,就都是质数
p = 2000000
d = [True]*p
n = list(range(2, p))
# print list(range(10))
for i in range(2, int(p**0.5)):
    #filter(lambda x:x%2!=0,n)
    for j in n:
        if j % i == 0:
            d[i] = False

#此bug也已经修复,麻烦测试,注意,还是先测试测试服.辛苦了.


