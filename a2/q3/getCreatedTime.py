import json
import datetime 
import dateutil.parser

now = datetime.datetime.now()
readCreatedTime = open('createdTime','r')
ageFile=open('UriWithAge.json','w')
noEstimatedDatecounter =0
for line in readCreatedTime:
	data= json.loads(line)
	Age= {}
	AgeList =[]
	if len(data['Estimated Creation Date']) >0:
		Age['uri'] = data['URI']
		EstimatedDate= data['Estimated Creation Date']
		d1 = dateutil.parser.parse(EstimatedDate)
		nowDate =now.isoformat()
		d2 = dateutil.parser.parse(nowDate)
		days = abs((d2 - d1).days)
		Age['days'] = days
		ageFile.write(json.dumps(Age) + "\n")
		# print Age
	else:
		noEstimatedDatecounter +=1
ageFile.close()
		
print "URI's with no EstimatedDate",noEstimatedDatecounter

read= open('UriWithAge.json','r')
output= open('days.json','w')
for line in read:
	data=json.loads(line)
	# print data['days']
	output.write(str(data['days'])+"\n")
