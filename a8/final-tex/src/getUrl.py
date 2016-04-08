def get100BlogUrl():
	link = "http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117"
	set = Set()

	while len(set) < 100:
		r = requests.get(link,allow_redirects=True)
		uri= r.url
				
		if len(uri) > 0:
				uri = uri.lower()
				
				parsedUrl = urlparse.urlparse(uri)
				parsedUrl = parsedUrl.scheme + '://' + parsedUrl.netloc + '/'
				
				set.add(parsedUrl)
				print len(set)
				print parsedUrl
	return set
	
def writeUrlToFile(data):
	file= open('get100Urls','w')
	file.write('http://f-measure.blogspot.com/'+'\n')
	file.write('http://ws-dl.blogspot.com/'+'\n')
	
	for item in data:
		file.write(item+'\n')