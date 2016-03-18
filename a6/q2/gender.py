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
		# if "." in firstName:
			# firstInitial = firstName
		# else:
			# firstInitial = firstName[0] + "."
		# lastName = name[2]
		print "FirstName:"+firstName
		# print "FirstInitial:"+firstInitial
		# print "LastName:"+lastName
		url = "https://api.genderize.io/?name=" +firstName
		r = requests.get(url)
		genderData= r.content
		print genderData
		print type(genderData)
		list.append(r.content)
	# print list
	f1.write(str(list))
	
