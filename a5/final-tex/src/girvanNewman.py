from igraph import * 
from xml.etree import ElementTree
import sys

karateClubGraph = Graph.Read_GraphML("karate.GraphML")
folderName = "graphs"
color_dict={1:"#1E90FF" , 2:"#DC143C", 3:"black", 4:"green" , 5:"lightblue"}
 
def savePlot(filename, visual_style):
	plot(karateClubGraph, './'+folderName+ '/'+ filename + '.pdf', **visual_style)

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

def plotFactionKarateClubGraph():
	visual_style = {}
	visual_style["vertex_size"] = 20
	visual_style["vertex_label"] = karateClubGraph.vs["name"]
	visual_style["vertex_label_dist"] = 1
	visual_style["vertex_color"] = [color_dict[node] for node in karateClubGraph.vs["Faction"]]
	layout = karateClubGraph.layout("rt_circular")
	savePlot('FactionGraph', visual_style)

def findEdgeBetweenness():
	numberOfclusters = 0
	count = 0
	while True:
		count += 1 
		edgeBetweennessValue =karateClubGraph.edge_betweenness()
		max_edgeBetweennessValue = max(edgeBetweennessValue)
		edge = [idx for idx, edgeBetweenness in enumerate(edgeBetweennessValue) if edgeBetweenness == max_edgeBetweennessValue]
		for idx in edge:
			karateClubGraph.es[idx]["edge_color"] = "red"
			karateClubGraph.es[idx]["edge_width"] = 3

		plotGraph ("EdgeHighlightedGraph"+str(count))
		karateClubGraph.delete_edges(edge)
		clusters = karateClubGraph.clusters('weak')
		numberOfclusters = len(clusters)
		print clusters
		print numberOfclusters
		print "count:",count
		c=1
		for cluster in clusters:
			for vertex in cluster:
				karateClubGraph.vs[vertex]["vertex_color"] = color_dict[c]
			c = c+1
		plotGraph ("Graph with"+str(numberOfclusters)+"Groups", True)
		clusterCount = 1
		if numberOfclusters > 4:
			break
	
plotGraph("OriginalGraph")
plotFactionKarateClubGraph()
findEdgeBetweenness()