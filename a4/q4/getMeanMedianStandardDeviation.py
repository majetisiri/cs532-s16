import numpy as np

data = np.loadtxt('followingCount')

mean=np.average(data)
median=np.median(data)
standardDeviation=np.std(data)

f = open('MeanMedianStd','w')
f.write("mean:"+str(mean)+"\n")
f.write("median:"+str(median)+"\n")
f.write("standardDeviation:"+str(standardDeviation)+"\n")
# print "mean:",mean
# print "median:",median
# print "standardDeviation:",standardDeviation
