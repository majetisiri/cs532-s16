from sets import Set 
import requests
import json

f = open("1000uri.json","r")
file= open("status_CodeWithUriCount.json","w")
UriSet = Set()
uricounter = 0
codeDict = {}
for line in f:
	if uricounter<1000:
		link= line.strip()
		print link
		try:
			r = requests.get(link)
			print '[%s] %s' % (r.status_code, r.url)
			if r.status_code in codeDict:
				codeDict[r.status_code] += 1
			else:
				codeDict[r.status_code] = 1
				
		except Exception, e:
			print e
			continue
	uricounter += 1

file.write(json.dumps(codeDict))

file.close()