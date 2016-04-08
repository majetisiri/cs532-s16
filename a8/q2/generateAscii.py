import clusters

def generateAscii():

    # returns blog titles, words in blog (10%-50% boundaries), list of frequency info
    blognames,words,data=clusters.readfile('blogdata.txt') 

    # returns a tree of foo.id, foo.left, foo.right
    clust=clusters.hcluster(data)

    # walks tree and prints ascii approximation of a dendogram; distance measure is Pearson's r
    clusters.printclust(clust,labels=blognames) 

generateAscii()