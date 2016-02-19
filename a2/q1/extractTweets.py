'''
CS532: Introduction to Web Science

'''

import tweepy
import re
import json
import urllib2
import sys
import time
import requests
from sets import Set 

CONSUMER_KEY = 'wTSsHE3PTA3ZZPiaKHEiQnLtf'
CONSUMER_SECRET = 'UblYYCmNYIEffAY4T4QHGHXwAWMFqiueXdxf35xZFhoK3AECP1'
ACCESS_KEY = '157985123-WFvzlfDa8KStBZzevMfQBTM7fi8zKHYl2LQpTfGr'
ACCESS_SECRET = 'lSax0XLwIimJ4VVbuU5OY9BpBic4vsSFi0riAq3DPvTxU'

auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

tweetJsonFile = open("tweet.json","a")
tweetCounter = 0
search_results = tweepy.Cursor(api.search, q="tesla", lang="en").items(5000)

while True:	
	try:
		tweet = search_results.next()
		for tweet in search_results:	
			#print tweet._json['entities']['urls']
			tweetJson = {}
			tweetJson['id'] = tweet.id
			tweetJson['text'] = tweet.text
			urlList = []
			uriCount = 0
			tweetCounter += 1
			for entityObj in tweet._json['entities']['urls']:
				uriCount += 1
				urlList.append(entityObj['url'])
			if uriCount > 0:
			
				tweetJson['uri'] = urlList
				tweetJson['json'] = tweet._json
				tweetJsonFile.write(json.dumps(tweetJson) + "\n")
			if tweetCounter > 1000:
				break
	except tweepy.TweepError:
		print "waiting \n"
		time.sleep(60*15)
		continue
	except StopIteration:
		break
		
tweetJsonFile.close()
	
f = open("tweet.json","r")
file= open("uri.json","a")
count = 0
UriSet = Set([])
for line in f:
	data = json.loads(line)
	if len(data['uri']) > 0:
		count += 1
	link= data['uri'][0]
	try:
		r = requests.get(link)
		if r.history:
			for h in r.history:
				UriSet.add(r.url)
				# print '[%s] %s' % (h.status_code, h.url)
			# print '[%s] %s' % (r.status_code, r.url)
		else:
			# print '[%s] %s' % (r.status_code, r.url)
			UriSet.add(r.url)
	except Exception, e:
		print e
		continue

for item in UriSet:
	file.write("%s\n" %item)

print count

file.close()