import json
import datetime 
import dateutil.parser

f= open('mementoData.json','r')
f1 = open('allMementosA10','w')
count =0 

for line in f:
	count+=1 
	if count <1001:
		data= json.loads(line)
		f1.write(data['count']+'\n')

f1.close()

f= open('allMementosA10','r')
f1= open('allMementosA2','r')

