import tweepy
import commands
import json
import time


CONSUMER_KEY = "1QjOMB7IZ00zaTvPmZ6tUrR2R"
CONSUMER_SECRET = "4aolvqxZYw3XwyrzWjiHb6aFAlg7iNodyxmyiIyX8NowefLL53"
ACCESS_KEY = "2820592280-iVQDNegTG1CtQLuQ14N9kwIefiVPSTA75zAKeye"
ACCESS_SECRET = "oaUFcXLImxaL0XGUvy3nT1XfBXkVkLNWDmRHkWvvDCozi"

auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# f1=open('sourceTarget','w')

def getSource():
	read=open('nodesData','r')
	data= json.load(read)
	list= []
	for user in range(0,len(data)):
		sourceScreenName= data[user]["screenName"]
		for user1 in range(user,len(data)-1):
			targetScreenName = data[user1+1]["screenName"]
			checkSourceFollowersAndFollowing(sourceScreenName,targetScreenName)
				
def checkSourceFollowersAndFollowing(sourceScreenName,targetScreenName):
	dict= {}
	count = 0
	dict['source']= sourceScreenName
	dict['target']= targetScreenName
	f1.write(json.dumps(dict)+",\n")	
	

def getAllLinks():
	f2 = open('linksData','w')
	read = open('sourceTarget','r')	
	data= json.load(read)
	for user in data:
		dict= {}
		sourceScreenName= user["source"]
		targetScreenName= user["target"]
		result = api.show_friendship(source_screen_name=sourceScreenName, target_screen_name=targetScreenName)
		dict['followed_by'] =result[0].followed_by
		dict['following'] =result[0].following
		dict['screen_name1']= result[0].screen_name
		dict['screen_name2']= result[1].screen_name
		f2.write(json.dumps(dict)+",\n")

def getTrueLinks():
	read = open('linksData','r')
	f2 = open('trueLinksData','w')	
	data= json.load(read)
	for user in data:
		dict = {}
		if user["following"] == True:
			dict['source']= user["screen_name1"]
			dict['target']= user["screen_name2"]
			f2.write(json.dumps(dict)+",\n")
		elif user["followed_by"]== True:
			dict['source']= user["screen_name2"]
			dict['target']= user["screen_name1"]
			f2.write(json.dumps(dict)+",\n")
	
def passTrueLinksSourceAndTarget():
	read = open('trueLinksData','r')
	data= json.load(read)
	for user in data:
		getIds(user["source"],user["target"])
			
def getIds(name1,name2):
	read = open('nodesData','r')
	f2 = open('linkIds','a')
	data= json.load(read)
	for user in data:
		dict ={}
		if name1 == user["screenName"]:
			id = user["id"]
			# print name1
			dict['source'] = id
			f2.write(json.dumps(dict)+",\n")
		elif name2 == user["screenName"]:
			id = user["id"]
			# print name2
			dict['target'] = id
			f2.write(json.dumps(dict)+",\n")
	f2.close()
# getSource()
# getAllLinks()
# getTrueLinks()
passTrueLinksSourceAndTarget()