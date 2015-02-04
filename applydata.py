import urllib.request
from bs4 import BeautifulSoup

req =  urllib.request.urlopen('http://www.1point3acres.com/bbs/')
the_page = req.read()
unicode_page = the_page.decode("utf-8")
parser = BeautifulSoup(unicode_page)
print (parser.title)