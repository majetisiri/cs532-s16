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