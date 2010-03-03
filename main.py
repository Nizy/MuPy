from xgoogle.search import GoogleSearch, SearchError
import os, commands
stermsartist = raw_input("Artist: ")
stermsalbum = raw_input("Album: ")
linklist = []
try:
    gs = GoogleSearch(stermsartist + stermsalbum + " site:http://www.megaupload.com")    
    gs.results_per_page = 5
    results = gs.get_results()    
    for res in results:      
        print res.desc.encode('utf8')
        print res.url.encode('utf8')
        linklist.append(res.url)
        print
except SearchError, e:
    print "Search failed: %s" % e
    
#DEBUGfor res in linklist:
    #print res
linkcount = len(linklist)
print "Select a link by number, from 0 to " + str(linkcount - 1)
linkselect = raw_input("Selection: ")
chosenlink = linklist[int(linkselect)]

slimrat = "/home/desperatefoe/Downloads/slimrat-1.0/src/slimrat"
slimcmd = slimrat + " " + chosenlink

os.system(slimcmd)
output = commands.getoutput(slimcmd)
print output



