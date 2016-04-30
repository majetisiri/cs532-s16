import os 

path = "/home/smajeti/coursework/cs532/a10/q4/A2/rawData/" 
# path = "/home/smajeti/coursework/cs532/a10/q4/A2/processedData/"
file1 = open('rawDataSize','w')
dirs = os.listdir( path )

for file in dirs:
	# print file
	path1 = path + file
	print path1
	size= os.path.getsize(path1)
	file1.write(str(size)+'\n')