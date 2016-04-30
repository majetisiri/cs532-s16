import os 

# path = "/home/smajeti/coursework/cs532/a10/q4/rawData/" 
path = "/home/smajeti/coursework/cs532/a10/q4/processedData/"
file1 = open('processedDataSize','w')
dirs = os.listdir( path )

for file in dirs:
	# print file
	path1 = path + file
	print path1
	size= os.path.getsize(path1)
	file1.write(str(size)+'\n')