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