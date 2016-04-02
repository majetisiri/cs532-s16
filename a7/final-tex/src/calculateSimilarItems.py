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