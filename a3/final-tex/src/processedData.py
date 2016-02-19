import commands
import os 

count = 0
input=open('uri.json','r')
t=open('command','w')
for line in input:
	count +=1 
	if count <1001:
		filename= str(count) + '-processed'
		# print str(line)
		command ='lynx -dump -force_html ' + '"'+ str(line).rstrip('\n') + '"'+'> ./processedData/' + filename
		# t.write(str(command))
		print command
		output = commands.getoutput(command)
input.close()

