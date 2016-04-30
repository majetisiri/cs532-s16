import commands
import os 

count = 0
input=open('1000uri.json','r')
t=open('command','w')
for line in input:
	count +=1 
	if count <1001:
		filename= str(count)
		# print str(line)
		command ='curl ' + '"' + str(line).rstrip('\n') + '"'+ '> ./rawData/' + filename
		# print command
		# t.write(str(command))
		output = commands.getoutput(command)
input.close()

