
def getData(path='./data/movielens/'):
	# DONE
	ratingDataFile = open("ratingData.json","w")
	ratingData ={}
	for line in open(path + 'u.data'):
		(user, movieid, rating, ts) = line.split('\t')
		ratingData['user'] = user.strip()
		ratingData['movieid'] = movieid.strip()
		ratingData['rating'] = rating.strip()
		# ratingData['ts'] = ts.strip()
		ratingDataFile.write(json.dumps(ratingData)+",\n")
		
	# DONE
	moviesDataFile = open("movieData.json","w")
	movies = {}
	for line in open(path + 'u.item'):
		movie_id = line.split('|')[0:1][0]
		movie_name = line.split('|')[1:2][0]
		movies['movie_id'] = re.sub(r'[^\x00-\x7F]',' ', movie_id)
		movies['movie_name'] = re.sub(r'[^\x00-\x7F]',' ', movie_name)
		moviesDataFile.write(json.dumps(movies) + ',\n')	
	
	
	# DONE
	userDataFile = open("userData.json","w")
	UserData = {}
	for line in open(path + 'u.user'):
		UserData['user_id'] = line.split('|')[0]
		userDetails = {}
		userDetails['age'] = line.split('|')[1]
		userDetails['occupation'] = line.split('|')[3]
		userDetails['gender'] = line.split('|')[2]
		UserData['user_details']= userDetails
		ratingDataFile = open("ratingData.json","r")
		ratingData = json.load(ratingDataFile)
		movieDetails_list = []
		for user1 in ratingData:
			r_id = user1['user']
			if UserData['user_id'] == r_id:
				movieDetails= {}
				movieDetails['movie_id'] = user1['movieid']
				movieDetails['movie_rating'] = user1['rating']
				moviesDataFile = open("movieData.json","r")
				movieData = json.load(moviesDataFile)
				for user2 in movieData:
					movie_id = user2['movie_id']
					if user1['movieid'] == movie_id:
						movieDetails['movie_name'] = user2['movie_name']
						break
				moviesDataFile.close()
				movieDetails_list.append(movieDetails)
		ratingDataFile.close()
		UserData['movie_details']= movieDetails_list
		userDataFile.write(json.dumps(UserData) + ',\n')