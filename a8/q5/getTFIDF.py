import feedparser
import re
import sys
import math

def getwordcounts(url):
  # Parse the feed
	d=feedparser.parse(url)
	wc={}

  # Loop over all the entries
	for e in d.entries:
		if 'summary' in e: 
			summary=e.summary
		else:
			summary=e.description

		# Extract a list of words
		words=getwords(e.title+' '+summary)
		for word in words:
			wc.setdefault(word,0)
			wc[word]+=1
	print d.feed.title
	return d.feed.title,wc

def getwords(html):
	# Remove all the HTML tags
	txt=re.compile(r'<[^>]+>').sub('',html)

	# Split words by all non-alpha characters
	words=re.compile(r'[^A-Z^a-z]+').split(txt)

	# Convert to lowercase
	return [word.lower() for word in words if word!='']
	
def generateFeedVector():
	apcount={}
	wordcounts={}
	iteration = 1
	feedlist=[line for line in file('getAtomsFor100Urls')]
	for feedurl in feedlist:
		try:
			title,wc=getwordcounts(feedurl)
			wordcounts[title]=wc
			for word,count in wc.items():
				apcount.setdefault(word,0)
				if count>1:
					apcount[word]+=1
		except:
			print 'Failed to parse feed %s' % feedurl
		iteration+=1
	
	wordlist=[]
	countFrequentWords=[]
	for w,bc in apcount.items():
		frac=float(bc)/len(feedlist)
		if frac>0.1 and frac<0.5:
			 countFrequentWords.append((w,bc))

	countFrequentWords=sorted(countFrequentWords,key=lambda x:x[1], reverse = True)

	for value in countFrequentWords:
		# word
		value1 = value[0]
		#count
		value2 = value[1]
		length = len(wordlist)
		if(length < 500):   
		  wordlist.append(value1)
		else:
		  break
		  
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
			if word in wc: 
				#tf for this word:
				termFrequency = wc[word]/float(len(wc))
				#idf
				inverseDocumentFrequency = logBase2(iteration/float(apcount[word]))

				#tfidf
				tfIdf = termFrequency*inverseDocumentFrequency

				#print '...tfIdf', tfIdf

				out.write('\t%f' % tfIdf)
			else:
				out.write('\t0')
		out.write('\n')

def logBase2(number):
	return math.log(number) / math.log(2)
	
generateFeedVector()