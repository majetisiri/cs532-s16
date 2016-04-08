def getBlogPagesURLs(url, blogUrlList=[]):
	req = requests.get(url)
	soup = BeautifulSoup(req.text)
	nextLink = soup.find('link', rel='next',href = True)
	if nextLink is not None:
		nextLink = nextLink['href']
		blogUrlList.append(nextLink)
		getBlogPagesURLs(nextLink, blogUrlList)
	return blogUrlList

def getwordcounts(url):
  d=feedparser.parse(url)
	wc={}

	for e in d.entries:
		if 'summary' in e: 
			summary=e.summary
		else:
			summary=e.description
			
		words=getwords(e.title+' '+summary)
		for word in words:
			wc.setdefault(word,0)
			wc[word]+=1
	print d.feed.title
	return d.feed.title,wc

def getwords(html):
	txt=re.compile(r'<[^>]+>').sub('',html)
	words=re.compile(r'[^A-Z^a-z]+').split(txt)
	return [word.lower() for word in words if word!='']

def combineWC(wc, nextwc):
	if len(wc)>0 and len(nextwc)>0:
		for word, wordcount in nextwc.items():
			if word in wc:
				wc[word] = wc[word] + wordcount
			else:
				wc[word] = wordcount
		return wc
	else:
		return {}
	
def generateFeedVector():
	apcount={}
	wordcounts={}
	feedlist=[line for line in open('getAtomsFor100Urls')]
	for feedurl in feedlist:
		try:
			blogUrlList = getBlogPagesURLs(feedurl)
			title,wc=getwordcounts(feedurl)
			for url in blogUrlList:
				title,nextwc=getwordcounts(feedurl)
				combineWC(wc,nextwc)
			wordcounts[title]=wc
			for word,count in wc.items():
				apcount.setdefault(word,0)
				if count>1:
					apcount[word]+=1
		except:
			print 'Failed to parse feed %s' % feedurl
	
	wordlist=[]
	countFrequentWords=[]
	for w,bc in apcount.items():
		frac=float(bc)/len(feedlist)
		if frac>0.1 and frac<0.5:
			 countFrequentWords.append((w,bc))

	countFrequentWords=sorted(countFrequentWords,key=lambda x:x[1], reverse = True)

	for value in countFrequentWords:
		value1 = value[0]
		value2 = value[1]
		length = len(wordlist)
		if(length < 500):   
		  wordlist.append(value1)
		else:
		  break
		
	stop_words_list = [line.rstrip('\r\n') for line in open('stopWordList.txt')]

	out=file('blogdata.txt','w')
	out.write('Blog')
	for word in wordlist: 
		word1 = word.encode('UTF-8')
		out.write('\t%s' % word1)
	out.write('\n')
	for blog,wc in wordcounts.items():
		blogName = blog.encode('UTF-8')
		print blog
		print blogName
		out.write(blogName)
		for word in wordlist:
		    if word not in stop_words_list:
				if word in wc: 
					out.write('\t%d' % wc[word])
				else:
					out.write('\t0')
		out.write('\n')