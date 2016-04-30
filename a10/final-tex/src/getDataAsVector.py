import json
f= open('blogdata.txt','r')
output = open('dataAsVector','w')
list1 = []
count = 0
for line in f:
	count += 1
	if count >1:  
		dict = {}
		line = line.strip()
		list = line.split('\t')
		blogName= list[0]
		list.pop(0)
		vector = list
		dict[blogName] = vector
		list1.append(dict)
output.write(json.dumps(list1))
