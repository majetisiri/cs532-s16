from random import random,randint
import math
import json

def cosineDistance(v1,v2):
  "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
  sumxx, sumxy, sumyy = 0, 0, 0
  for i in range(0,len(v1)-1):
    x = int(v1[i]); y = int(v2[i])
    sumxx += x*x
    sumyy += y*y
    sumxy += x*y
  return sumxy/math.sqrt(sumxx*sumyy)


def getdistances(data,vec1):
  distancelist=[]
  
  for i in data:
    for subitem in i:
      if subitem != 'F-Measure':
        vec2= i[subitem]
    
    distancelist.append((cosineDistance(vec1,vec2),i))
  distancelist.sort()
  return distancelist

def knnestimate(data,vec1,k=5):
  dlist=getdistances(data,vec1)
  avg=0.0
  for i in range(k):
    idx=dlist[i]
    print idx
	
def main():
	f= open('dataAsVector','r')
	data = json.load(f)
	for item in data:
		for subitem in item:
			if subitem == 'F-Measure':
				vec1= item[subitem]
				knnestimate(data,vec1)
			
main()