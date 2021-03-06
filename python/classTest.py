import random, json, codecs
from testFunctions import listShuffler
from pprint import *

class CharacterSheet(object):
    "For learning"
    _instances = set()

    def __init__(self, t):

        self.file = "data/" + t + ".json"
        self.t = t
        self.data = json.load(codecs.open(self.file, "r", "utf-8-sig"))
        self.namelist = [self.data[t][n]["name"] for n in range(len(self.data[t])) if self.data[t][n]["source"] == "PHB" or self.data[t][n]["source"] == "XGE" or self.data[t][n]["source"] == "VGM"]
        rtd = random.randint(0,len(self.namelist)-1)
        self.name = self.namelist[rtd]
        self.index = [self.data[t][n]["name"] for n in range(len(self.data[t]))].index(self.name)
        self.__class__._instances.add(self)
        return

    def getProfs(self):
        self.profs = []
        if self.t == "race":
            raceSkillData = self.data["race"][self.index]
            if "proficiency" in raceSkillData:
                self.profs.append(raceSkillData["proficiency"])
        if self.t == "class":
            classSkillData = self.data["class"][self.index]["startingProficiencies"]["skills"]
            if "choose" in classSkillData:
                self.profs.extend(listShuffler(classSkillData["from"], classSkillData["choose"]))
            else:
                self.profs.extend(self.data[self.t][self.index]["startingProficiencies"])
            self.profs.extend([self.data["class"][self.index]["proficiency"][x].title() + " Saving Throws" for x in range(2)])
        if self.t == "background":
            self.profs.append(self.data[self.t][self.index]["skillProficiencies"])

        del self.data, self.namelist # we are done with the huge dicts "data" and "namelist" for now

        return self.profs

#     def pushJson(self):
#         jsonPush = {}
#         jsonPush ["Stats"] = {
#        "beforeRaceBonus": statslist,
#         "afterRaceBonus": racialStats(raceStuff)[0]
#         }
#         jsonPush [self.t.title()] = {
#             self.t + "name": self.name,
#             self.name + "Proficiencies" = self.profs
#
#         }
#
#         if self.t == "race"
#             jsonPush [self.t.title()] = {
#             "name": self.name,
#             "raceProficiencies": self.profs
#             }
#         elif self.t =="Class"] = {
#         "name": classStuff,
#         "subclass": None,
#         "classProficiencies": getStuff("class", classStuff)
#         }
#         jsonPush ["Background"] = {
#         "name": backgroundStuff,
#         "backgroundProficiencies": getStuff("background", backgroundStuff)
#         }
#
#         if featStuff != None:
#             jsonPush ["Feat"] = {
#             "name": featStuff
#             }

        #PrettyPrinter(indent=2).pprint(jsonPush)

        with open("sheets/" + raceStuff + " " + classStuff + " " + backgroundStuff + ".json", "w") as f:
            f.write(json.dumps(jsonPush, indent=2))


testrace = CharacterSheet("race")
testclass = CharacterSheet("class")
testbackground = CharacterSheet("background")
proficiencies = testrace.getProfs() + testclass.getProfs() + testbackground.getProfs()
print(testrace.name + " " + testclass.name + " " + testbackground.name)
print(proficiencies)

print(list(CharacterSheet._instances)[0].__dict__)



#PrettyPrinter(indent=2).pprint(testrace.__dict__)
#PrettyPrinter(indent=2).pprint(testclass.__dict__)
#PrettyPrinter(indent=2).pprint(testbackground.__dict__)
