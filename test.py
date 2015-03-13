from pyquery import PyQuery as pq
from lxml import etree
import urllib
import sys
print (sys.version)

class DataGrab:

	univer_info = None # university information
	date_info = None # post date
	msg_id = "" # message id
	msg_link = "" # message link
	msg_author = "" # message author's name
	msg_authorlink = "" # message author's link
	web_url = "" # url need to be grabbed

	#class init
	def __init__(self, web_url): 
		self.web_url = web_url
	
	#grab the university and post date info from a string
	def univer_grab(self, para_info):
		split_string = para_info.replace(" " , "").split("]")
		self.univer_info =  split_string[1].replace("[", "").split("@")
		self.date_info = split_string[2].split("-")

	def grad_grab(self, raw_info):
		raw_info = raw_info('.pcb')
		print('-----------------------------------------------')
		info_list = raw_info('li:eq(0)').text()
		print(info_list.replace("[", "").split(":",1))
		#print(info_list[0].replace(" " , "").split(":"))
		




	#do the grab job
	def data_process(self):
		raw_data = pq(url=self.web_url)

		for i in raw_data('#threadlisttableid').items("tbody"): #grab every row in the bbs
	
			if "normalthread" in i.attr("id") : #some post may have no id
				self.msg_id = i.attr("id")
				self.msg_link = i('.icn a').attr("href")
				self.author = i(".by a").html()
				self.msg_authorlink = i(".by a").attr("href")

				if type(i('.new')) != type(None):
					raw_info = i('.new span').text()
					self.univer_grab(raw_info)
				else:
					raw_info = i('.common span').text()
					self.univer_grab(raw_info)
				
				detail_anal = pq(url = self.msg_link) # grab the author's grade
				self.grad_grab(detail_anal)
				
				#self.info_display()	
				

	
	def info_display(self):
		print("id:" + self.msg_id)
		print("link:" + self.msg_link)
		print("author:" + self.msg_author)
		print("author_link:" + self.msg_authorlink)	
		print(self.date_info)
		#print("date:" + self.date_info[1] + "." + self.date_info[2] + "." + self.date_info[3])
		print(self.univer_info)	

begin_grab = DataGrab('http://www.1point3acres.com/bbs/forum-82-1.html')
begin_grab.data_process()


