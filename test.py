from pyquery import PyQuery as pq
from lxml import etree
import urllib

d = pq(url='http://www.1point3acres.com/bbs/forum-82-1.html')
print('hello')
print(d("#threadlisttableid"))
print("over")