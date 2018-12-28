import os
from os import listdir
from os.path import isfile, join
import re
from collections import defaultdict
import unittest

#This program looks into the autorun.md file included with Uniview Profiles.
#Scans over all UV profiles, gets autorun.md file.
#Isolates module names
#Matches the module names to the profile name in a hash?
#Writes the profile name to the appropriate module in the csv list for dataTables

profilesPath = '../../Profiles'

#Gets the names of all the profile folders 
def getFolderNames():
    directories = os.listdir(profilesPath)
    return directories
def getValidProfileNames():
    directories = getFolderNames()
    validProfileNames = []
    for profile in directories:  
        subpath = os.path.join(profilesPath, profile,"Modules")
        if(os.path.exists(subpath)):
            #print os.listdir(subpath)
            validProfileNames.append(profile)
    return validProfileNames

#returns list of profiles with autorun files available
#the list has profile relative paths, its not just the profile names by itself
def getAutorunFiles():
    directories = getValidProfileNames()
    validProfilePaths = []
    for profile in directories:  
        subpath = os.path.join(profilesPath, profile,"Modules")
        validProfilePaths.append(os.path.join(subpath,"autorun.mod"))
    return validProfilePaths

def getSingleAutorunFilePath(profilename):
    subpath = os.path.join(profilesPath, profilename,"Modules")
    if(os.path.exists(subpath)):
        
        return os.path.join(subpath,"autorun.mod")
        
#open the autorun file for a given profile
def readAutorunMod(filepath):
    ###DELETEvalidProfiles = getAutorunFiles()
    #just getting the first valid file for testing
    #TODO, make forloop that iterates over validProfiles
    ###DELETEthefirstfilepath = validProfiles[0]
    thefirstfilepath = filepath
    
    currentFile = open(thefirstfilepath,"r")
    FiletoText= currentFile.read()
    #Use regular expression to get load{} list of modules that are loaded
    justthemodules= re.findall('(?=.*load)[^{]+{[^}]+}',FiletoText)[0]

    #Get a list of only the module names
    modulesSingleLines = justthemodules.split("\n")
    unwantedchars = {'load','{','}'}
    reduceModuleList = [item for item in modulesSingleLines if item not in unwantedchars]
    reduceModuleList = [item[4:] for item in modulesSingleLines]
    
    EXTRAreduceModuleList=[]
    for x in reduceModuleList:
        #print x
        theshortname= re.findall('(.*\/)', x)
        if theshortname:
            shortname=theshortname[0]
            EXTRAreduceModuleList.append(shortname)
            
    EXTRAreduceModuleList = [item[:-1] for item in EXTRAreduceModuleList]
    EXTRAreduceModuleList = [item[1:] if item[0]=="*" else item for item in EXTRAreduceModuleList]

    return EXTRAreduceModuleList

def addtoMaster(modulename, profilename, masterDict):
    #if profilename not in masterDict:
    masterDict.setdefault(modulename, []).append(profilename)
    return masterDict
#Merges modules to the dict of modules that will be written to the master dictionary
#returns a dictionary of key-values
def organizeToDictionary(profilename, path):
    #the module folder names
    ModuleList = readAutorunMod(path)
    masterDict = {}
    for module in ModuleList:
        addtoMaster(module, profilename, masterDict)
    return masterDict

#combines the above functions together
#gets the valid profiles containing autorun files
#sends a profile name to readAutorunMod
#that function returns a list of the module names for that profile
#sends module list and profile name to organizeToDctionary, which adds the profile to the modules
#in the module list.

def master():
    ProfileList = getValidProfileNames()
    #print ProfileList
    FinalDict = defaultdict(list)
    for profile in ProfileList:
        path = getSingleAutorunFilePath(profile)
        #print path, "is the path"
        #ModuleList = readAutorunMod(path)
        currentDict = organizeToDictionary(profile,path)
        for key,value in currentDict.iteritems():
            FinalDict[key]+=value
        #FinalDict = organizeToDictionary(profile, path)
    #print FinalDict        
    return FinalDict


#Unit tests down here
class MyTest(unittest.TestCase):
    def test(self):
        getsDirectories = type(getFolderNames()) is list
        self.assertTrue(getsDirectories, True)
if __name__ == '__main__':
    unittest.main()
    
#readAutorunMod()
#organizeToDictionary()
#master()
