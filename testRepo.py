import urllib2
import json
import os

def updateTests(dataDirectory = "", filename = "tests.json", url = "http://haileon.com/SimTyrantJS_ListTestCases"):
    fileDest = dataDirectory + filename
    print("Getting " + url + " ...")
    resp = urllib2.urlopen(url=url)
    contents = resp.read()
    print("Saving " + fileDest + " ...")
    with open(fileDest, 'wb') as f:
        f.write(contents)
    return contents

def loadTests(forceUpdate = False, dataDirectory = "", filename = "tests.json", url = "http://haileon.com/SimTyrantJS_ListTestCases"):
    data = None
    if(not forceUpdate):
        fileDest = os.path.join(dataDirectory, filename)
        if(os.path.exists(fileDest)):
            with open(fileDest, 'rb') as f:
                data = f.read()
    if(data is None):
        data = updateTests(dataDirectory, filename, url)
    json_data = json.loads(data)
    decks = json_data["decks"]
    return decks

def printTestFailure(expected, actual, key, comment):
    print("TEST FAILED on " + key + " (" + str(expected) + " vs. " + str(actual) + "): " + comment)

def testKey(deck, key, actual):
    testThreshold = 10
    if(key in deck):
        expected = deck[key]
        if((expected == 100 or expected == 0) and expected != actual):
            printTestFailure(expected, actual, key, deck["comments"])
        elif((expected + testThreshold) < actual or (expected - testThreshold) > actual):
            printTestFailure(expected, actual, key, deck["comments"])
