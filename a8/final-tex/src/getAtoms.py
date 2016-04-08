def getAtoms():
	file= open('get100Urls','r')
	f1= open('getAtomsFor100Urls','w')
	add= "feeds/posts/default?max-results=500"
	for uri in file:
		uri= uri.strip()+add 
		f1.write(uri+"\n")