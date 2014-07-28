#!/usr/bin/python
# Your Task: Find the five most post-apocalyptic
# pothole-filled 10-block sections of road in Chicago.
# Bonus: Identify the worst road based on historical
# data involving actual number of patched potholes.
# import modules as needed
import csv
import re 
def whatsMyBlock (addr):
# reduce address to the block.
    parts = addr.split()
    block = ''
    if not parts: 
        print addr, 'invalid address data'
        return 'invalid address data'
    # handle 2 to 6 digit blocks
    if len(parts[0]) == 2:
        block = parts[0][0] + '0'
    elif len(parts[0]) == 3:
        block = parts[0][0] + '00'
    elif len(parts[0]) == 4:
        block = parts[0][0] + parts[0][1] + '00'
    elif len(parts[0]) == 5:
        block = parts[0][0] + parts[0][1] + parts[0][2] + '00'
    elif len(parts[0]) == 6:
        block = parts[0][0] + parts[0][1] + parts[0][2] + parts[0][3] + '00'
    elif len(parts[0]) == 1:
        block = '000'
    else :
        print addr, "does not seem to have block data"
        return addr
    parts.pop(0)
    if block: # if block data successfully assigned
        while parts:
            block += " " + parts.pop(0)
    else:
        print addr, 'invalid address data, failed to assign block'
        return 'invalid address data'
    return block

def onlyLookFirst(t):
    a ,b = t
    return a
def main():
    #getdata from csv
    #f = open('data\\potholesshort.csv')
    f = open('data\\potholes.csv')
    potholes_by_block = {}  # a dict with blocks as keys and count of potholes as data
    for row in csv.DictReader(f):
        addr = row['STREET ADDRESS']
        num = row['NUMBER OF POTHOLES FILLED ON BLOCK']
        #print addr , ' had ' , num
        block = whatsMyBlock(addr)
        if not block in potholes_by_block.keys() :
            potholes_by_block[block] = 0
        #needs exception handling for bad data.
        #check to see if num has numeric data
        regularOldHoles = re.search(r'(\d+)', num)
        if regularOldHoles:
            potholes_by_block[block] += int(regularOldHoles.group(1)) + 1 #add it if its there
            #print "historic data found for", block, int(regularOldHoles.group(1))
        else:
            potholes_by_block[block] += 1 # otherwise just add one.

    #print potholes_by_block
    # listize the data, sort it, print the top 10 blocks.
    listOfHoledPlaces = []
    for b in potholes_by_block.keys():
        tupleHole = (potholes_by_block[b], b )
        listOfHoledPlaces.append( tupleHole )
    sortedListOfHoledPlaces = sorted(listOfHoledPlaces, key=onlyLookFirst, reverse=True )
    place = 0
    while place < 10:
        print str(place + 1), sortedListOfHoledPlaces[place] 
        place = place + 1
    
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()