from operator import sub
f1= open('processedDataSize','r')
f2= open('A2/processedDataSize', 'r')
f3= open('differenceProcessedDataSize', 'w')

list = []
list1 =[]
resultList= []

for line in f1:
	list.append(int(line.strip()))
	
for line in f2:
	list1.append(int(line.strip()))

resultList = [a - b for a, b in zip(list, list1)]

for item in resultList:
	f3.write(str(item)+'\n')