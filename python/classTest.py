import random, json, codecs
from testFunctions import *

class classObject(object):
    "For learning"
    file = "data/class.json"
    data = json.load(codecs.open(file, "r", "utf-8-sig"))

    def __init__(self): # This returns just the name of the randomly p

            return
    def picker(self):
        with codecs.open(self.file, "r", "utf-8-sig") as data_file:
            namelist = [self.data["class"][n]["name"] for n in range(len(self.data["class"])) if self.data["class"][n]["source"] == "PHB" or self.data["class"][n]["source"] == "XGE" or self.data["class"][n]["source"] == "VGM"]
            rtd = random.randint(0,len(namelist)-1)
            return namelist[rtd]

testclass = classObject()

print(testclass)
