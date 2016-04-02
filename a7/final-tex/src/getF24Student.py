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