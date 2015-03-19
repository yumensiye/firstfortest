from pyquery import PyQuery as pq
from lxml import etree
import urllib
import sys
print (sys.version)

class DataGrab:

	univer_info = "" # university information
	notice_date = "" # post date
	msg_id = "" # message id
	msg_link = "" # message link
	msg_author = "" # message author's name
	msg_authorlink = "" # message author's link
	web_url = "" # url need to be grabbed
	post_date = "" #post date
	author_info = "" #author info


	#class init
	def __init__(self, web_url): 
		self.web_url = web_url
	
	#grab the university and post date info from a string
	def univer_grab(self, para_info):
		split_string = para_info.replace(" " , "").split("]")
		#print(split_string)
		#self.univer_info =  split_string[1].replace("[", "")
		self.univer_info =  split_string[1].replace("[", "")
		tmp_list = []
		tmp_list = split_string[2].split("-")
		if len(tmp_list) >= 4:
			self.notice_date = tmp_list[1] + "-" + tmp_list[2] + "-" + tmp_list[3]
			self.author_info = tmp_list[4]


	def grad_grab(self, raw_info):
		raw_info = raw_info('.pcb')
		print('-----------------------------------------------')
		info_list = raw_info('li:eq(0)').text()
		print(info_list.replace("[", "").split(":",1))
		print(type(info_list.replace("[", "").split(":",1)[1]))
		#print(info_list[0].replace(" " , "").split(":"))
		




	#do the grab job
	def data_process(self):
		raw_data = pq(url=self.web_url)

		for i in raw_data('#threadlisttableid').items("tbody"): #grab every row in the bbs
	
			if "normalthread" in i.attr("id") : #some post may have no id
				self.msg_id = i.attr("id")
				self.msg_link = i('.icn a').attr("href")
				self.msg_author = i(".by a").html()
				self.post_date = i(".by em span span").attr("title")
				if type(self.post_date) == type(None):
					self.post_date = i(".by em span").html()
				self.msg_authorlink = i(".by a").attr("href")

				if type(i('.new')) != type(None):
					raw_info = i('.new span').text()
					self.univer_grab(raw_info)
				else:
					raw_info = i('.common span').text()
					self.univer_grab(raw_info)
				
				#detail_anal = pq(url = self.msg_link) # grab the author's grade
				#self.grad_grab(detail_anal)
				
				self.info_display()	
				

	
	def info_display(self):
		print("id:" + self.msg_id)
		print("link:" + self.msg_link)
		print("author:" + self.msg_author)
		print("author_link:" + self.msg_authorlink)	
		print("author_info:" + self.author_info)
		print("notice_date:" + self.notice_date)
		print("univer_info:" + self.univer_info)
		print("post_date:" + self.post_date)
		#print(self.notice_date)
		#print("date:" + self.notice_date[1] + "." + self.notice_date[2] + "." + self.notice_date[3])
		#print(self.univer_info)	

begin_grab = DataGrab('http://www.1point3acres.com/bbs/forum-82-1.html')
begin_grab.data_process()


