import requests
from bs4 import BeautifulSoup

def news():
	# the target we want to open	
	# url='http://nagios.beta-wspbx.com/nagios/cgi-bin/extinfo.cgi?type=2&host=beta-161&service=Freeswitch'
	# url='http://192.168.1.8/wsvn/'
	url='http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service&hostname=10.30.48.183&servicedescription=Streams'
	
	#open with GET method
	resp=requests.get(url)
	
	#http_respone 200 means OK status
	if resp.status_code==200:
		print("Successfully opened the web page")
		print("------------ :-\n")
	
		# # we need a parser,Python built-in HTML parser is enough .
		# soup=BeautifulSoup(freeswitch.txt,'html.parser')	

		# # l is the list which contains all the text i.e news
		# l=soup.find("div",{"class":"dataVar"})
	
		# #now we want to print only the text part of the anchor.
		# #find all the elements of a, i.e anchor
		# for i in l.findAll("div"):
		# 	print(i.text)
	else:
		print("Error")
		
news()
