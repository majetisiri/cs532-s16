import json

def getImdbName():
	f = open("imdbRating","r")
	data = json.load(f)
	for user in data:
		if user['rating'] != 'N/A':
			print float(user['rating'])/2, user['name']

def average():
	f = open("averageRank","r")
	data = json.load(f)
	for user in data:
		print round(float(data[user]['average']),2), data[user]['movie_name']

average()