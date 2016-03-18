import tweepy
import sys
import json
import time

CONSUMER_KEY = 'wTSsHE3PTA3ZZPiaKHEiQnLtf'
CONSUMER_SECRET = 'UblYYCmNYIEffAY4T4QHGHXwAWMFqiueXdxf35xZFhoK3AECP1'
ACCESS_KEY = '157985123-WFvzlfDa8KStBZzevMfQBTM7fi8zKHYl2LQpTfGr'
ACCESS_SECRET = 'lSax0XLwIimJ4VVbuU5OY9BpBic4vsSFi0riAq3DPvTxU'

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
	f.write(json.dumps(userData)+"\n")
	f.close()

f1 = open('linksData','w')
read = open('nodesData','r')
def links():
	userData =[]
	for line in read:
		data= json.loads(line)
		for user in data:
			dict = {}
			dict['source'] = user['id']
			dict['target'] =  0
			userData.append(dict)
	f1.write(json.dumps(userData)+"\n")
	f1.close()

nodes()
links()