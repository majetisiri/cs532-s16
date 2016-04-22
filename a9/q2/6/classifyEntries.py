import docclass
import feedfilter

def main():
    cl=docclass.fisherclassifier(docclass.getwords) 
    cl.setdb('majeti.db')
    print "testing the program"
    feedfilter.read('input.xml',cl)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)