from operator import sub
f1= open('allMementosA10','r')
f2= open('allMementosA2', 'r')
f3= open('differenceTimeMaps', 'w')

list = []
list1 =[]
resultList= []

for line in f1:
	list.append(int(line.strip()))
	
print list
	

for line in f2:
	list1.append(int(line.strip()))

print list1

resultList = [a - b for a, b in zip(list, list1)]
print resultList

for item in resultList:
	f3.write(str(item)+'\n')