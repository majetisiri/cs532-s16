import clusters

def drawDendogram():
	blognames,words,data=clusters.readfile('blogdata.txt') 
	clust=clusters.hcluster(data) 
	clusters.drawdendrogram(clust,blognames,jpeg='blogclust.jpg') 

drawDendogram()