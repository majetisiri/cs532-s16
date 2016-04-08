import clusters

def getKmeans():
	blognames,words,data=clusters.readfile('blogdata.txt') 
	print "K value is 5"
	kclust=clusters.kcluster(data,k=5)
	print "\t\t"+str([blognames[r] for r in kclust[0]]) # print blognames in 1st centroid
	print "\t\t"+str([blognames[r] for r in kclust[1]]) # print blognames in 2nd centroid
	print "\t\t"+str([blognames[r] for r in kclust[2]])# print blognames in 3rd centroid
	print "\t\t"+str([blognames[r] for r in kclust[3]]) # print blognames in 4th centroid
	print "\t\t"+str([blognames[r] for r in kclust[4]]) # print blognames in 5th centroid
	print "K value is 10"
	kclust=clusters.kcluster(data,k=10)
	print "\t\t"+str([blognames[r] for r in kclust[0]]) # print blognames in 1st centroid
	print "\t\t"+str([blognames[r] for r in kclust[1]]) # print blognames in 2nd centroid
	print "\t\t"+str([blognames[r] for r in kclust[2]])# print blognames in 3rd centroid
	print "\t\t"+str([blognames[r] for r in kclust[3]]) # print blognames in 4th centroid
	print "\t\t"+str([blognames[r] for r in kclust[4]]) # print blognames in 5th centroid
	print "\t\t"+str([blognames[r] for r in kclust[5]]) # print blognames in 6th centroid
	print "\t\t"+str([blognames[r] for r in kclust[6]]) # print blognames in 7th centroid
	print "\t\t"+str([blognames[r] for r in kclust[7]]) # print blognames in 8th centroid
	print "\t\t"+str([blognames[r] for r in kclust[8]]) # print blognames in 9th centroid
	print "\t\t"+str([blognames[r] for r in kclust[9]]) # print blognames in 10th centroid
	print "K value is 20"
	kclust=clusters.kcluster(data,k=20)
	print "\t\t"+str([blognames[r] for r in kclust[0]]) # print blognames in 1st centroid
	print "\t\t"+str([blognames[r] for r in kclust[1]]) # print blognames in 2nd centroid
	print "\t\t"+str([blognames[r] for r in kclust[2]])# print blognames in 3rd centroid
	print "\t\t"+str([blognames[r] for r in kclust[3]]) # print blognames in 4th centroid
	print "\t\t"+str([blognames[r] for r in kclust[4]]) # print blognames in 5th centroid
	print "\t\t"+str([blognames[r] for r in kclust[5]]) # print blognames in 6th centroid
	print "\t\t"+str([blognames[r] for r in kclust[6]]) # print blognames in 7th centroid
	print "\t\t"+str([blognames[r] for r in kclust[7]]) # print blognames in 8th centroid
	print "\t\t"+str([blognames[r] for r in kclust[8]]) # print blognames in 9th centroid
	print "\t\t"+str([blognames[r] for r in kclust[9]]) # print blognames in 10th centroid
	print "\t\t"+str([blognames[r] for r in kclust[10]]) # print blognames in 11th centroid
	print "\t\t"+str([blognames[r] for r in kclust[11]])# print blognames in 12th centroid
	print "\t\t"+str([blognames[r] for r in kclust[12]]) # print blognames in 13th centroid
	print "\t\t"+str([blognames[r] for r in kclust[13]]) # print blognames in 14th centroid
	print "\t\t"+str([blognames[r] for r in kclust[14]]) # print blognames in 15th centroid
	print "\t\t"+str([blognames[r] for r in kclust[15]]) # print blognames in 16th centroid
	print "\t\t"+str([blognames[r] for r in kclust[16]]) # print blognames in 17th centroid
	print "\t\t"+str([blognames[r] for r in kclust[17]]) # print blognames in 18th centroid
	print "\t\t"+str([blognames[r] for r in kclust[18]]) # print blognames in 19th centroid
	print "\t\t"+str([blognames[r] for r in kclust[19]]) # print blognames in 20th centroid
	
getKmeans()