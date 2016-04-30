import commands
import re
import json
import sys
 
def geturi():
	file=open("uri.json","r")
	uricounter = 0
	for line in file:
		if uricounter <1000:
			f = open('PagesList','w')
			response = getPages(line)
			f.write(response)
			f.close()
			finalCount =getMementosData()
			uricounter += 1
	file.close()
	
def getPages(uri):
	timemapUri = "http://mementoproxy.cs.odu.edu/aggr/timemap/link/1/"
	command ="curl -i --silent " + timemapUri + str(uri).strip()

	pageList = commands.getoutput(command)
	return pageList
	
def getMementosData():
	getMementosDataFile = open("PagesList","r")
	outputfile= open('mementoData.json', 'a')
	mementoList= []
	mementoJson ={}
	Json ={}
	count = 0
	for line in getMementosDataFile:
		if 'rel="original"' in line:
			count = 0
			originalLink =  (re.findall(r'(https?://[^\s]+>)', line))[0][:-1]
			Json['originaluri'] = originalLink
			print Json
		if 'rel="memento"' in line:
			count += 1
			link = ""
			if re.findall(r'(https?://[^\s]+>)', line):
				link =  (re.findall(r'(https?://[^\s]+>)', line))[0][:-1]
			elif re.findall(r'(www.[^\s]+>)', line):
				link =  (re.findall(r'(www.[^\s]+>)', line))[0][:-1]
			else:
				print line
			mementoId = count
			mementoJson['mementouri'] = link
			mementoJson['id'] =mementoId
			if(line.find('datetime="') > -1):
				datetime = (line.split('datetime="'))[1].split('"')[0]
				mementoJson['datetime'] =datetime
			mementoList.append(mementoJson)
			Json['memento'] = mementoList
	finalCount = str(count) 
	Json['count'] = finalCount
	outputfile.write(json.dumps(Json) + "\n")
	
geturi()

