import requests
import json

BASE_URL = 'http://www.omdbapi.com/'
MAX_RATING = 5

#removes all the junk and returns the name of the movie in correct format
def parseMovieName(movieName):
	movie = movieName.strip().split('(')
	name = movie[0].split(',')
	try:
		movieName = name[1].strip() + ' ' + name[0].strip()
	except IndexError:
		movieName = name[0].strip()
	return movieName

#api call returns json with movie rating
def getRatingFromIMDb(movieName):
	movie = parseMovieName(movieName)
	params = dict(i='',t=movie.lower())
	r = requests.get(BASE_URL, params=params)
	# print r.content
	data = json.loads(r.content)
	dictionary = {}
	if data['Response'] == 'True':
		dictionary['rating'] = data['imdbRating']
		dictionary['votes'] = data['imdbVotes']
		dictionary['name'] = movieName.replace('"',"'")
		return dictionary, 0
	else:
		dictionary['rating'] = -1
		return dictionary, 1

#highest = maximum rating in the list.
#lowest = minimum rating in the list.
#currentRating = rating to be normalized
#temp is multiplied by MAX_RATING for normalizing it to scale of MAX_RATING.
def normalizeRatings(highest, lowest, currentRating):
	temp = float(currentRating - lowest)/float(highest - lowest)
	return temp * MAX_RATING

COUNT = 0
w = open('imdbRating','a')
f = open('u.item','r')
ratingList = []
for line in f:
	data = line.split('|')
	ratingData, count = getRatingFromIMDb(data[1])
	if count == 0:
		ratingList.append(ratingData)
		w.write(json.dumps(ratingData) + ',\n')
	else:
		COUNT += 1
		print 'MovieLens Name:' + data[1], ', Processed Name:' + parseMovieName(data[1]) + '--\n'

print COUNT

