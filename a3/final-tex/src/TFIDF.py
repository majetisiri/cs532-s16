import json
import math 

totalNumberOfDocumentInCorpus =47000000000
documentWithTerm = 3520000000

def calculate(): 
	input  = open('selected10URIsWithSrtingAndWordCount.json','r')
	for line in input:
		data= json.loads(line)
		TF = round((float(data['numberOfOccurrencesOfStringInDoc'])/float(data['totalWordsInDoc'])),3)
		print 'TF:', TF
		IDF = round(logBase2( float(totalNumberOfDocumentInCorpus) / float(documentWithTerm) ),3)
		print 'IDF:',IDF
		TFIDF = round((TF*IDF),3)
		print 'TFIDF:',TFIDF
			
def logBase2(number):
	return math.log(number) / math.log(2)

calculate()