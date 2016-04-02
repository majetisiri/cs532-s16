import json

def getMovieName(id):
	moviesDataFile = open("movieData.json","r")
	movieData = json.load(moviesDataFile)
	for user in movieData:
		if user['movie_id'] == id:
			return user['movie_name']
		
def rankBasedOnMovieLense():
	f = open('averageRank','w')
	ratingDataFile = open("ratingData.json","r")
	ratingData = json.load(ratingDataFile)
	count = 0
	siri_dic = {}
	for user in ratingData:
		rating = user['rating']
		movie_id = user['movieid']
		user_id = user['user']
		if movie_id in siri_dic:
			siri_dic[movie_id]['rating'] = siri_dic[movie_id]['rating'] + int(rating)
			siri_dic[movie_id]['count'] = siri_dic[movie_id]['count'] + 1
			siri_dic[movie_id]['average'] = siri_dic[movie_id]['rating'] * 1.0 / siri_dic[movie_id]['count']
		else:
			siri_dic[movie_id] = {'rating': int(rating), 'count': 1, 'average': rating, 'movie_name': getMovieName(movie_id)}
	f.write(json.dumps(siri_dic) + ',\n')
rankBasedOnMovieLense()

