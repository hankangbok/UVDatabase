from collections import defaultdict


#ModuleList = ["module1", "module2", "module 3", "module 4"]
#profile1 = "profile1"
#profile2 = "profile2"
def addtoMaster2(modulename, profilename, masterDict):
    #if profilename not in masterDict:
    masterDict.setdefault(modulename, []).append(profilename)
    return masterDict
#masterDict = {}

#for module in ModuleList:
#    addtoMaster(module, profile1, masterDict)
#    addtoMaster(module, profile2, masterDict)
#print masterDict

##originalDict = {'module 3': ['profile123'], 'module 5': ['profile2'], 'module2': ['profile2'], 'module1': ['profile1', 'profile2']}
#mergedDict = defaultdict(list)
#for item in (masterDict, originalDict):
 #   for key, value in item.iteritems():
  #      mergedDict[key].append(value)
    
#print mergedDict
