import requests
import json 

def function(input):
	LastName = name.split()
	
read=open('nodesData','r')
f1= open('gender','w')
list = []
for line in read:
	data= json.loads(line)
	for user in data:
		name = (str(user['name']))
		print "\n"+name
		name = name.partition(" ")
		firstName = name[0]
		print "FirstName:"+firstName
		url = "https://api.genderize.io/?name=" +firstName
		r = requests.get(url)
		genderData= r.content
		print genderData
		print type(genderData)
		list.append(r.content)
	f1.write(str(list))
	
