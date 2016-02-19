import json
import math 

totalNumberOfDocumentInCorpus =47000000000
documentWithTerm = 3520000000

def calculate(): 
	input  = open('selected10URIsWithSrtingAndWordCount.json','r')
	o = open('TFIDFvalues','w')
	for line in input:
		data= json.loads(line)
		name = data['filename']
		TF = round((float(data['numberOfOccurrencesOfStringInDoc'])/float(data['totalWordsInDoc'])),3)
		o.write(name +"\n")
		print 'TF:', TF
		o.write('TF:'+ str(TF) +"\n")
		IDF = round(logBase2( float(totalNumberOfDocumentInCorpus) / float(documentWithTerm) ),3)
		o.write('IDF:'+ str(IDF) +"\n")
		print 'IDF:',IDF
		TFIDF = round((TF*IDF),3)
		o.write('TFIDF:' + str(TFIDF) +"\n")
		print 'TFIDF:',TFIDF
			
def logBase2(number):
	return math.log(number) / math.log(2)

calculate()