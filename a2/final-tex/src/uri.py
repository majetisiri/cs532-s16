'''
CS532: Introduction to Web Science
Author: Srividya Majeti
Assignment 2
'''

import json

f= open('data.json','r')
f1 = open('urisWithMementosExcluding0','w')
f2 = open('allMementos','w')
f3=open ('mementosExcluding0','w')
for line in f:
	data= json.loads(line)
	f2.write(data['count'] + "\n")
	if data['count'] != "0":
		f1.write(line)
		f3.write(data['count'] + "\n")