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

f = open('userFollowingData','w')
def get_followers():
	users = []
	page_count = 0
	userData = []
	for user in tweepy.Cursor(api.friends, screen_name='ohttic').items():
		usr = {}
		usr['screen_name'] = user.screen_name
		usr['followers_count'] = user.followers_count
		usr['friends_count'] = user.friends_count
		page_count += 1
		userData.append(usr)
		print str(page_count)
	f.write(str(json.dumps(userData)))
	f.close()
		
get_followers()