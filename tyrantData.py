import hashlib
import urllib2
import os

def getCheck(dataDirectory = ""):
    check = {}
    files = ["achievements", "cards", "missions", "quests", "raids"]
    for filename in files:
        path = os.path.join(dataDirectory, filename + ".xml")
        if os.path.exists(path):
            with open(path, 'rb') as f:
                contents = f.read()
            md5hash = hashlib.md5(contents).hexdigest()
            check[filename] = md5hash
    return check

def updateDataFiles(source = "http://kg.tyrantonline.com", dataDirectory = "", files = ["achievements", "cards", "missions", "quests", "raids"]):
    print("Getting data from " + source)
    for filename in files:
        url = source + "/assets/" + filename + ".xml"
        fileDest = dataDirectory + filename + ".xml"
        print("Getting " + url + " ...")
        resp = urllib2.urlopen(url=url)
        contents = resp.read()
        print("Saving " + fileDest + " ...")
        with open(fileDest, 'wb') as f:
            f.write(contents)
