import tweepy
import sys
import json
import time

# siri
CONSUMER_KEY = 'wTSsHE3PTA3ZZPiaKHEiQnLtf'
CONSUMER_SECRET = 'UblYYCmNYIEffAY4T4QHGHXwAWMFqiueXdxf35xZFhoK3AECP1'
ACCESS_KEY = '157985123-WFvzlfDa8KStBZzevMfQBTM7fi8zKHYl2LQpTfGr'
ACCESS_SECRET = 'lSax0XLwIimJ4VVbuU5OY9BpBic4vsSFi0riAq3DPvTxU'

# # bharath
# CONSUMER_KEY = "qhJBwYCG9nYR7d5a5ZNfJD3Wy"
# CONSUMER_SECRET = "gWAh87ScdyhUE5weUNc7PvLsc2Lax2yLm6sGKOjIbxELnfcKBS"
# ACCESS_KEY = "2801896164-B9QLY4qwRBDKzi0LH1e1utgywvPrYdDOHJHnG0i"
# ACCESS_SECRET = "ATnP7537AG1Q6tNgvwnekprYz5vpYgj7jykxRGYEgo8nX"

# masroor
# CONSUMER_KEY = 'CfHUyBhlMaLv5Mn8r2IziXpLs'
# CONSUMER_SECRET = 'PqqtbhbyNb5mcJ2dHkSIT2wupOMuEqfSINGYvV8KDIOPuqgDkN'
# ACCESS_TOKEN = '29202483-qK6twPLeurVc8Ls8zBxdFtaFGyzm76LUBbtXOMMk1'
# ACCESS_TOKEN_SECRET = 'aOIFdI1TVJjsIPWNO1rAFx2IECzVSCPY4kOnEKBA0pCdA'

auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

f = open('nodesData','w')
def nodes():
	count = 1
	page_count= 0
	userData = []
	for user in tweepy.Cursor(api.followers, screen_name='majetisiri').items():
		usr = {}
		usr['screenName'] = user.screen_name
		usr['name'] =  user.name
		usr['id'] =  count
		usr['img'] =  user.profile_image_url
		usr['link'] = "https://twitter.com/"+user.screen_name
		usr['size'] =  40000
		page_count += 1
		userData.append(usr)
		count+= 1
		# print str(page_count)
	f.write(json.dumps(userData)+"\n")
	f.close()

# f1 = open('linksData','w')
# read = open('nodesData','r')
def links():
	userData =[]
	for line in read:
		data= json.loads(line)
		for user in data:
			# print (str(user['id'])+ "\n")
			dict = {}
			dict['source'] = user['id']
			dict['target'] =  0
			userData.append(dict)
	f1.write(json.dumps(userData)+"\n")
	f1.close()

nodes()
# links()