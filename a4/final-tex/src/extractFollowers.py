import json

read=open('userFollowerData','r')
f1= open('followersCount','w')
for line in read:
	data= json.loads(line)
	for user in data:
		f1.write(str(user['followers_count']) +"\n")
		