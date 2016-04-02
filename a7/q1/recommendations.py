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

# Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs,person1,person2):
  # Get the list of shared_items
  si={}
  for item in prefs[person1]: 
    if item in prefs[person2]: si[item]=1

  # if they have no ratings in common, return 0
  if len(si)==0: return 0

  # Add up the squares of all the differences
  sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) 
                      for item in prefs[person1] if item in prefs[person2]])

  return 1/(1+sum_of_squares)

# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs,p1,p2):
  # Get the list of mutually rated items
  si={}
  for item in prefs[p1]: 
    if item in prefs[p2]: si[item]=1

  # if they are no ratings in common, return 0
  if len(si)==0: return 0

  # Sum calculations
  n=len(si)
  
  # Sums of all the preferences
  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])
  
  # Sums of the squares
  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si])	
  
  # Sum of the products
  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
  
  # Calculate r (Pearson score)
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0

  r=num/den

  return r

# Returns the best matches for person from the prefs dictionary. 
# Number of results and similarity function are optional params.
def topMatches(prefs,person,n=5,similarity=sim_pearson):
  scores=[(similarity(prefs,person,other),other) 
                  for other in prefs if other!=person]
  scores.sort()
  scores.reverse()
  return scores[0:n]

# Gets recommendations for a person by using a weighted average
# of every other user's rankings
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
        totals[item]+=prefs[other][item]*sim
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


def calculateSimilarItems(prefs,n=10):
  # Create a dictionary of items showing which other items they
  # are most similar to.
  result={}
  # Invert the preference matrix to be item-centric
  itemPrefs=transformPrefs(prefs)
  c=0
  for item in itemPrefs:
    # Status updates for large datasets
    c+=1
    if c%100==0: print "%d / %d" % (c,len(itemPrefs))
    # Find the most similar items to this one
    scores=topMatches(itemPrefs,item,n=n,similarity=sim_distance)
    result[item]=scores
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

def loadMovieLens(path='/data/movielens'):
  # Get movie titles
  movies={}
  for line in open(path+'/u.item'):
    (id,title)=line.split('|')[0:2]
    movies[id]=title
  
  # Load data
  prefs={}
  for line in open(path+'/u.data'):
    (user,movieid,rating,ts)=line.split('\t')
    prefs.setdefault(user,{})
    prefs[user][movies[movieid]]=float(rating)
  return prefs
 
 
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
		
				
def getFemaleUsers():
	f = open('listOfFemaleUsers','w')
	userDataFile = open("userData.json","r")
	userData = json.load(userDataFile)
	# femaleUsers=[]
	count = 0
	countF = 0
	for user in userData:
		count += 1
		if user['user_details']['gender'] =='F':    #gives only female users
			countF += 1
			f.write(json.dumps(user) + ',\n')
	print "Total users:" +str(count)
	print "number of female users:" +str(countF)
	
	
	
def getFemaleUsersWithAgeCloserto24():
	f = open('listOfFemaleUsers','r')
	userData = json.load(f)
	f1 = open('listOfFemaleUsersWithAgeCloserTo24','w')
	# femaleUsersWithAge24=[]
	count24 = 0
	countF = 0
	for user in userData:
		countF += 1
		if user['user_details']['age'] < '26' and user['user_details']['age'] >'21':
			count24 += 1
			f1.write(json.dumps(user) + ',\n')
	print "number of female users:" +str(countF)
	print "number of female users with age 24:" +str(count24)
	
def getFemaleUsersWithAgeCloserto24AndStudent():
	f = open('listOfFemaleUsersWithAgeCloserTo24','r')
	userData = json.load(f)
	f1 = open('listOfFemaleUsersWithAge24AndStudent','w')
	count24 = 0
	countStudent = 0
	for user in userData:
		count24 += 1
		if user['user_details']['occupation']=='student':
			countStudent+= 1
			f1.write(json.dumps(user) + ',\n')
	print "number of female users with age 24:" +str(count24)
	print "number of female users with age 24 and Student:" +str(countStudent)

def topRatedAndLeastRated():
	f = open('myList.json','r')
	f1 = open('myListWithMovies.json','w')
	userData = json.load(f)
	dict= {}
	for user in userData:
		dict['user_id'] = user['user_id']
		for movie in user['movie_details']:
			if movie['movie_rating'] =='5':
				dict['type'] ='Top Rated'
				dict['movie_id']=movie['movie_id']
				dict['movie_name']=movie['movie_name']
				dict['movie_rating']=movie['movie_rating']
				f1.write(json.dumps(dict) + ',\n')
			if movie['movie_rating'] =='1' or movie['movie_rating'] =='2' :
				dict['type'] ='Least Rated'
				dict['movie_id']=movie['movie_id']
				dict['movie_name']=movie['movie_name']
				dict['movie_rating']=movie['movie_rating']
				f1.write(json.dumps(dict) + ',\n')
				
# getData()	
# getFemaleUsers()
# getFemaleUsersWithAgeCloserto24()
# getFemaleUsersWithAgeCloserto24AndStudent()
topRatedAndLeastRated()