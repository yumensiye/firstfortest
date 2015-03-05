from pyquery import PyQuery as pq
from lxml import etree
import urllib
import sys
print (sys.version)

raw = pq(url='http://www.1point3acres.com/bbs/forum-82-1.html')

summary_data = raw('#threadlisttableid')

for i in summary_data:
	#print(i)
	print (pq(i).find('.icn'))