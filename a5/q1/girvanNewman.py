from igraph import * 
from xml.etree import ElementTree
import sys

karateClubGraph = Graph.Read_GraphML("karate.GraphML")
folderName = "graphs"
color_dict={1:"#1E90FF" , 2:"#DC143C", 3:"black", 4:"green" , 5:"lightblue"}
# save graph 
def savePlot(filename, visual_style):
	plot(karateClubGraph, './'+folderName+ '/'+ filename + '.pdf', **visual_style)

# plotting original graph and edge hoghlighted graph
def plotGraph(filename, vertColorChanged=False):
	visual_style = {}
	visual_style["vertex_size"] = 20
	visual_style["vertex_label"] = karateClubGraph.vs["name"]
	visual_style["vertex_label_dist"] = 1
	if vertColorChanged == True:
		print "Color Changed"
		visual_style["vertex_color"] = [vert["vertex_color"] for vert in karateClubGraph.vs]
	visual_style['edge_color'] = [edgeColor for edgeColor in karateClubGraph.es['edge_color']]
	visual_style['edge_width'] = [edgeWidth for edgeWidth in karateClubGraph.es['edge_width']]
	if vertColorChanged == True:
		print visual_style
	layout = karateClubGraph.layout("rt_circular")
	savePlot(filename, visual_style)

# plotting graph that distinguishes groups with colors based on factions 
def plotFactionKarateClubGraph():
	visual_style = {}
	visual_style["vertex_size"] = 20
	visual_style["vertex_label"] = karateClubGraph.vs["name"]
	visual_style["vertex_label_dist"] = 1
	visual_style["vertex_color"] = [color_dict[node] for node in karateClubGraph.vs["Faction"]]
	layout = karateClubGraph.layout("rt_circular")
	savePlot('FactionGraph', visual_style)
	
#find edgebetweenness, maximum edgebetweenness and connection having highest betweenness centrality
def findEdgeBetweenness():
	numberOfclusters = 0
	count = 0
	while True:
		count += 1 
		edgeBetweennessValue =karateClubGraph.edge_betweenness()
		#print "edgeBetweennessValue:",edgeBetweennessValue
		max_edgeBetweennessValue = max(edgeBetweennessValue)
		#print "max_edgeBetweennessValue:",max_edgeBetweennessValue
		edge = [idx for idx, edgeBetweenness in enumerate(edgeBetweennessValue) if edgeBetweenness == max_edgeBetweennessValue]
		for idx in edge:
			karateClubGraph.es[idx]["edge_color"] = "red"
			karateClubGraph.es[idx]["edge_width"] = 3

		#print edge
		plotGraph ("EdgeHighlightedGraph"+str(count))
		karateClubGraph.delete_edges(edge)
		clusters = karateClubGraph.clusters('weak')
		numberOfclusters = len(clusters)
		print clusters
		print numberOfclusters
		print "count:",count
		c=1
		for cluster in clusters:
			# color = color_dict[c]
			# print color
			# print "Cluster Length: ", len(cluster)
			for vertex in cluster:
				# print "new vertex"
				karateClubGraph.vs[vertex]["vertex_color"] = color_dict[c]
				# if numberOfclusters > 1:
				# 	for vert in karateClubGraph.vs:
				# 		print vert['vertex_color']

			# sys.exit(-9)
			c = c+1
		# if numberOfclusters>1:
		# 	sys.exit(-9)
		plotGraph ("Graph with"+str(numberOfclusters)+"Groups", True)
		clusterCount = 1
		if numberOfclusters > 4:
			break
	
#plotGraph("OriginalGraph")
plotFactionKarateClubGraph()
findEdgeBetweenness()