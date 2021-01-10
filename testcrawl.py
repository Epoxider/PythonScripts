#Matthew Fritz

from bs4 import BeautifulSoup
import requests
import re
from collections import deque


WIKI_BASE='https://en.wikipedia.org'

def internal_not_special(href):
    if href:
        if re.compile('^/wiki/').search(href):
            if not re.compile('/\w+:').search(href):
                if not re.compile('#').search(href):
                    return True

def getrandURL(): #generates random URL to start at
    #r = requests.get(WIKI_BASE+'/wiki/George_Lucas')   # Found in 1 hop with breadth first, 2 hops depth first
    #r = requests.get(WIKI_BASE+'/wiki/Mellody_Hobson')  # Found in 2 hops breadth first, ?? depth first
    r = requests.get(WIKI_BASE+'/wiki/Special:Random')

    return r.url

def printResults(item, desired_title, max_depth): #prints final links to get to desired title
    if not item:
        print("\nWent past depth="+str(max_depth)+" and didn't find '"+str(desired_title)+"': stopping..")
        return 

    l = []
    while(item):
        l.insert(0, item[0])
        item = item[2]

    indent = 0
    print()
    for url in l:
        r = requests.get(WIKI_BASE+url)
        page = BeautifulSoup(r.text, 'html.parser')
        pageTitle = page.find('h1', id='firstHeading').string

        print("  "*indent+str(pageTitle)+" ("+WIKI_BASE+url+")")
        indent += 1

def familyString(item): # shows parent links
    s = ""
    if not item:
        return s
    s = item[0]
    item = item[2]

    while(item):
        s += " <- " + item[0]
        item = item[2]

    return s

#implemented a DFS also to see if the run time was any faster, turned out it was slower given the starting page
#George lucas but faster given Mellody Hobson
def depthFirst(item, visited_urls_set, desired_title, max_depth):

    url = item[0]
    depth = item[1]

    if url in visited_urls_set:
        return None

    visited_urls_set.add(url)

    r = requests.get(WIKI_BASE+url)

    page = BeautifulSoup(r.text, 'html.parser')

    pageTitle = page.find('h1', id='firstHeading').string

    print("  "*depth+str(depth)+" : "+familyString(item))

    if( pageTitle == desired_title ):
        return item

    if( depth+1 <= max_depth ):
        mainBody = page.find(id = 'bodyContent')

        for link in page.find_all('a', href=internal_not_special):
            href = link.get('href')
            newitem = depthFirst([href, depth+1, item], visited_urls_set, desired_title, max_depth)
            if( newitem ):
                return newitem
return None 

#Here is the BFS
def breadthFirst(item, visited_urls_set, desired_title, max_depth):
    queue = deque()
    queue.append( item )

    while len(queue):
        item = queue.popleft()
        url = item[0]
        depth = item[1]

        if( depth > max_depth ):
            break

        if url in visited_urls_set:
            continue

        visited_urls_set.add(url)

        r = requests.get(WIKI_BASE+url)

        page = BeautifulSoup(r.text, 'html.parser')

        pageTitle = page.find('h1', id='firstHeading').string

        print("  "*depth+str(depth)+" [Q-size="+str(len(queue))+"] : "+familyString(item))

        if( pageTitle == desired_title ):
            return item
 
        mainBody = page.find(id = 'bodyContent')
        for link in page.find_all('a', href=internal_not_special):
            href = link.get('href')
            if not href in visited_urls_set:
                queue.append( [href, depth+1, item] )

    return None


#startURL = getrandURL()
startURL = "https://en.wikipedia.org/wiki/George_Lucas"
startURL = startURL[len(WIKI_BASE):]

print('URL: ' + WIKI_BASE + startURL)

item = [startURL, 0, None]

visited_urls_set = set()
max_depth = 6
desired_title="Horizon Zero Dawn" # Was also thinking of doing Mass Effect, Portal, or even the new Tomb Raider Games
# Or maybe even an oldie like roller coaster Tycoon

item = breadthFirst(item, visited_urls_set, desired_title, max_depth)
#item = depthFirst(item, visited_urls_set, desired_title, max_depth)

printResults(item, desired_title, max_depth)
