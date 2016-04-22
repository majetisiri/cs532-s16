import docclass
import feedfilter

def main():
    cl=docclass.fisherclassifier(docclass.getwords) 
    cl.setdb('smajeti.db')
    print "testing the program"
    feedfilter.read('toiEntertainment.xml',cl)
