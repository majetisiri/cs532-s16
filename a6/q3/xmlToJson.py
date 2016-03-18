from xml.etree import ElementTree
import json

with open('karate.GraphML', 'rt') as f:
	f1= open('karateClub.json','w')
	tree = ElementTree.parse(f)
	root = tree.getroot()
	print root
	data = {}
	data1={}
	nodes = []
	links= []
	count = 0
	f1.write('{' + '\n' + '"nodes":\n' + '[' +"\n" )
	for parent in root:
		# print parent.tag, parent.attrib
		for child in parent:
			# print child.tag, child.attrib
			if child.tag == ('{http://graphml.graphdrawing.org/xmlns}node'):
				id = child.get('id')
				print "id:",id	
				for children in child:
					if children.attrib.get('key') == 'name':
						name= children.text
						print "name:",name
						data["name"] = name
						f1.write(json.dumps(data)+',\n')
					if children.attrib.get('key') == 'Faction':
						Faction= children.text
						print "Faction:",Faction
						data["faction"] = int(Faction)
						data["color"] = 1
						# f1.write(json.dumps(data)+',\n')
	f1.write('],' + '\n' + '"links":\n' + '[' +"\n" )
	for parent in root:
		# print parent.tag, parent.attrib
		for child in parent:
			# print child.tag, child.attrib	
			if child.tag == ('{http://graphml.graphdrawing.org/xmlns}edge'):
				source = child.get('source')
				count +=1
				# print "source:",source
				data1["source"] = int(source)
				target = child.get('target')
				# print "target:",target
				data1["target"] = int(target)
				for children in child:
					if children.attrib.get('key') == 'weight':
						weight= children.text
						# print "weight:",weight
						data1["weight"] = int(weight)
						data1["id"] = "e"+str(count)
						f1.write(json.dumps(data1)+",\n")
	f1.write(']' + '\n' + "}")