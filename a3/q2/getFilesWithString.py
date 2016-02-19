import os
import commands
import json

f = open('filenamesWithCount','w')
queryTerm = "food"
def getFilesWithString(queryTerm):
	filenamesCountJson ={}
	iterateThroughFiles = next(os.walk('./processedData/'))[2]
	print 'number of times %s found in files'%queryTerm 
	for filename in iterateThroughFiles:
		command = 'cat ' + './processedData/'+  filename + ' | grep -i -c ' + queryTerm
		numberOfOccurrencesInDoc = commands.getoutput(command)
		if numberOfOccurrencesInDoc > '0':
			filenamesCountJson['numberOfOccurrencesOfStringInDoc'] =numberOfOccurrencesInDoc
			filenamesCountJson['filename'] = filename
			command = 'cat ' + './processedData/'+  filename + ' | wc -w  '
			totalWords = commands.getoutput(command)
			filenamesCountJson['totalWordsInDoc'] =totalWords
			f.write(json.dumps(filenamesCountJson) + "\n")
getFilesWithString(queryTerm)