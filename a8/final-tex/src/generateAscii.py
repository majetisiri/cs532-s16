import clusters

def generateAscii():
    blognames,words,data=clusters.readfile('blogdata.txt') 
    clust=clusters.hcluster(data)
    clusters.printclust(clust,labels=blognames) 

generateAscii()