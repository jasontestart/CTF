#!/usr/bin/python2
# This script parses the Naughty and Nice List (CSV).
# For each person on the list, query the NPPD 
# infractions database and gather an infractions list.

# Written for the SANS Holiday Hack Challenge 2017
# by Jason Testart
# December 2017

import csv
import urllib2
import json

# Function: Given a name, return 'hits' from the NPPD database
def getInfractions(name):
    jsonQueryString = 'http://nppd.northpolechristmastown.com/infractions?query=name=%s&json=1'
    thisQuery = jsonQueryString % name.replace(' ','+')
    req = urllib2.Request(thisQuery)
    return urllib2.urlopen(req)

##
## MAIN
##
theListFileName = 'Naughty and Nice List.csv'
masterInfractionsList = []
with open(theListFileName, 'rb') as theListFile:
    theList = csv.reader(theListFile)
    for row in theList:
        infractionsList = ''
        infractionsList = json.load(getInfractions(row[0]))['infractions']
        if infractionsList:
            masterInfractionsList.extend(infractionsList)

outFileName = 'all_infractions.json'
outFile = open(outFileName, 'wb')
outFile.write(json.dumps(masterInfractionsList))
outFile.close
