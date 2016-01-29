import urllib2
import sys #to pass link as command line arguement
from bs4 import BeautifulSoup,SoupStrainer

uri= sys.argv[1]
request= urllib2.Request(uri)
response= urllib2.urlopen(request)
response.getcode()
soup = BeautifulSoup(response,"html5lib") 

def getsize(link):
	file= urllib2.urlopen(link)
	size=file.headers.get("content-length")
	type=file.headers.get("content-type")
	status=file.getcode()
	if status == 200 and type == "application/pdf":
		print "found a url with pdf in the link:",link
		print "size:",size,"bytes"
		print "status:",status
	file.close()

for link in soup.findAll('a'):
	getsize(link['href'])
	
