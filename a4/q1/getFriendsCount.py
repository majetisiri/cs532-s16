from xml.etree import ElementTree

with open('mln.graphml', 'rt') as f:
	f1= open('friendCount','w')
	tree = ElementTree.parse(f)
	root = tree.getroot()
	print root
	list=[]
	for parent in root:
		# print parent.tag, parent.attrib
		for child in parent:
			if child.tag == ('{http://graphml.graphdrawing.org/xmlns}node'):
				for children in child:
					try:
						if children.attrib.get('key') == 'name':
							name=children.text
							# f1.write("\n"+name +"\t")
					except:
						name = name.encode('ascii',errors='ignore')
						print name
						# f1.write("\n"+name +"\t")
					if children.attrib.get('key') == 'friend_count':
						friendCount=children.text
						if friendCount >0:
							f1.write(str(friendCount)+"\n")
							# list.append(friendCount)
						else:
							f1.write(" None \n")
	# f1.write(str(list))
	f1.close()


