# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

import json
import re
from math import sqrt
import sys
def sim_pearson(pref,p1,p2):
  # Get the list of mutually rated items
  si={}
  for item in pref[p1]: 
    if item in pref[p2]: si[item]=1

  # if they are no ratings in common, return 0
  if len(si)==0: return 0

  # Sum calculations
  n=len(si)
    
  sum1 = 0
  for it in si:
	sum1 =  sum1 + int(pref[p1][it])

  sum2 = 0
  for it in si:
	sum2 =  sum2 + int(pref[p2][it])

  sum1Sq = 0
  for it in si:
	sum1Sq =  sum1Sq + pow(int(pref[p1][it]),2)
  
  sum2Sq = 0
  for it in si:
	sum2Sq =  sum2Sq + pow(int(pref[p2][it]),2)

  
  pSum = 0  
  for it in si:
	pSum =  pSum + ( int(pref[p2][it]) * int(pref[p1][it]) )
	
  
  # Calculate r (Pearson score)
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0

  r=num/den

  return r


# Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs,person1,person2):
  # Get the list of shared_items
  si={}
  for item in prefs[person1]: 
    if item in prefs[person2]: si[item]=1

  # if they have no ratings in common, return 0
  if len(si)==0: return 0

  # Add up the squares of all the differences
  sum_of_squares=sum([pow(int(prefs[person1][item])- int(prefs[person2][item]),2) 
                      for item in prefs[person1] if item in prefs[person2]])

  return 1/(1+sum_of_squares)


# Returns the best matches for person from the prefs dictionary. 
# Number of results and similarity function are optional params.
def topMatches(prefs,person,n=5,similarity=sim_pearson,reverseSimilarityFlag=True):
  scores=[(similarity(prefs,person,other),other) 
                  for other in prefs if other!=person]
  scores.sort()
  
  if(reverseSimilarityFlag):
  
	scores.reverse()
  upperLimit = len(scores)
  lowerLimit = upperLimit - 5
  upperScores = scores[0:5]
  lowerScores = scores[lowerLimit:upperLimit]
  scoreResult = []
  for item in upperScores:
    scoreResult.append(item)
  for item in lowerScores:
    scoreResult.append(item)
# Gets recommendations for a person by using a weighted average
# of every other user's rankings
  return scoreResult

def getRecommendations(prefs,person,similarity=sim_pearson):
  totals={}
  simSums={}
  for other in prefs:
    # don't compare me to myself
    if other==person: continue
    sim=similarity(prefs,person,other)

    # ignore scores of zero or lower
    if sim<=0: continue
    for item in prefs[other]:
	    
      # only score movies I haven't seen yet
      if item not in prefs[person] or prefs[person][item]==0:
        # Similarity * Score
        totals.setdefault(item,0)
        totals[item] += int(prefs[other][item])*sim
        # Sum of similarities
        simSums.setdefault(item,0)
        simSums[item]+=sim

  # Create the normalized list
  rankings=[(total/simSums[item],item) for item,total in totals.items()]

  # Return the sorted list
  rankings.sort()
  rankings.reverse()
  return rankings

def transformPrefs(prefs):
  result={}
  for person in prefs:
    for item in prefs[person]:
      result.setdefault(item,{})
      
      # Flip item and person
      result[item][person]=prefs[person][item]
  return result


def calculateSimilarItems(prefs, movieName, simMeasure, n=10, reverseSimilarityFlag=True, transformMatrixFlag=True):
    '''
    Create a dictionary of items showing which other items they are
    most similar to.
    '''

    result = {}
    # Invert the preference matrix to be item-centric

    if( transformMatrixFlag ):
        #with transform: movie top similarity
        itemPrefs = transformPrefs(prefs)
    else:
        #without transform: user top similarity
        itemPrefs = prefs

    #c = 0
    for item in itemPrefs:
	    

        # Status updates for large datasets
        #c += 1
        #if c % 100 == 0:
            #print '%d / %d' % (c, len(itemPrefs))
        # Find the most similar items to this one
        scores = topMatches(itemPrefs, item, n=n, similarity=simMeasure, reverseSimilarityFlag=reverseSimilarityFlag)
        
        result[item] = scores
        if item.lower() in movieName.lower():
		    return result
    return result
		
def getRecommendedItems(prefs,itemMatch,user):
  userRatings=prefs[user]
  scores={}
  totalSim={}
  # Loop over items rated by this user
  for (item,rating) in userRatings.items( ):

    # Loop over items similar to this one
    for (similarity,item2) in itemMatch[item]:

      # Ignore if this user has already rated this item
      if item2 in userRatings: continue
      # Weighted sum of rating times similarity
      scores.setdefault(item2,0)
      scores[item2]+=similarity*rating
      # Sum of all the similarities
      totalSim.setdefault(item2,0)
      totalSim[item2]+=similarity

  # Divide each total score by total weighting to get an average
  rankings=[(score/totalSim[item],item) for item,score in scores.items( )]

  # Return the rankings from highest to lowest
  rankings.sort( )
  rankings.reverse( )
  return rankings

def loadMovieLens(path='./data/movielens'):
  # Get movie titles
  movies={}
  for line in open(path+'/u.item'):
    (id,title)=line.split('|')[0:2]
    movies[id]=title
  # Load data
  prefs={}
  count = 0
  for line in open(path+'/u.data'):
    (user,movieid,rating,ts)=line.split('\t')
    prefs.setdefault(user,{})
    prefs[user][movies[movieid]]=float(rating)
  return prefs, movies
 
 
def getData(path='./data/movielens/'):
	# DONE
	# ratingDataFile = open("ratingData.json","w")
	# ratingData ={}
	# for line in open(path + 'u.data'):
		# (user, movieid, rating, ts) = line.split('\t')
		# ratingData['user'] = user.strip()
		# ratingData['movieid'] = movieid.strip()
		# ratingData['rating'] = rating.strip()
		# # ratingData['ts'] = ts.strip()
		# ratingDataFile.write(json.dumps(ratingData)+",\n")
		
	# # DONE
	# moviesDataFile = open("movieData.json","w")
	# movies = {}
	# for line in open(path + 'u.item'):
		# movie_id = line.split('|')[0:1][0]
		# movie_name = line.split('|')[1:2][0]
		# movies['movie_id'] = re.sub(r'[^\x00-\x7F]',' ', movie_id)
		# movies['movie_name'] = re.sub(r'[^\x00-\x7F]',' ', movie_name)
		# moviesDataFile.write(json.dumps(movies) + ',\n')	
	
	
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


def correlation():
	userDataFile = open("userData.json","r")
	userData = json.load(userDataFile)
	
	correlation_dic = {}
	for user in userData:
		user_id = user['user_id']
		movie_details_dic = {}
		for movie in user['movie_details']:
			movie_id = movie['movie_id']
			movie_rating = movie['movie_rating']
			movie_details_dic[movie_id] = movie_rating
		correlation_dic[user_id] = movie_details_dic
	
	return correlation_dic	
	#correlationDataFile = open("correlationData.json","w")
	#correlationDataFile.write(json.dumps(correlation_dic) + '\n')


# getData()


	
#correlation_dic = correlation()
#user_min = []
#user_max = []
#max = [-10,-10,-10,-10,-10]
#min = [10,10,10,10,10]
#for user in correlation_dic:	
#	if(user != '711'):
#		result = sim_pearson(correlation_dic, '711', user)
#		if(max[0] < result):
#			max[0] = result
#			max.sort()
#			user_max.append(user)
#		if(min[0] > result):
#			min[0] = result
#			min.sort()
#			min.reverse()
#			user_min.append(user)

movieLensRating, moviesData = loadMovieLens()
MOVIE_NAME=moviesData['71']
result1 = calculateSimilarItems(movieLensRating, MOVIE_NAME,simMeasure=sim_pearson, n=10, reverseSimilarityFlag=True, transformMatrixFlag=True) 
item = result1[MOVIE_NAME]
print 'Top five correlated films for: ', MOVIE_NAME
for film in item[0:5]:
    print film
print 'Bottom five correlated films for: ', MOVIE_NAME
for film in item[5:10]:
    print film


#Duplicate code for second movie.
MOVIE_NAME=moviesData['771']
result1 = calculateSimilarItems(movieLensRating, MOVIE_NAME,simMeasure=sim_pearson, n=10, reverseSimilarityFlag=True, transformMatrixFlag=True) 
item = result1[MOVIE_NAME]
print 'Top five correlated films for: ', MOVIE_NAME
for film in item[0:5]:
    print film
print 'Bottom five correlated films for: ', MOVIE_NAME
for film in item[5:10]:
    print film
