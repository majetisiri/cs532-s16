import json

read=open('userFollowerData','r')
f2= open('followingCount','w')
for line in read:
	data= json.loads(line)
	for user in data:
		f2.write(str(user['friends_count'])+ "\n")