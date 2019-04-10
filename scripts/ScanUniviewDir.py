import os
from os import listdir
from os.path import isfile,join
import csv
import unittest
from bs4 import BeautifulSoup
import re
from collections import defaultdict

CustomModulesFolderPath = '..\..\custom modules'

#Generates a CSV table with the module names and empty columns otherwise

def notEmpty(aPath):
    return len(os.listdir(aPath))>0

# Checks if module includes a description.html file
def hasDescription(folderpath,module):
    modulePath = os.path.join(folderpath,module)
#Check that this module has a description .html in it subdirectories
    subdirs = os.listdir(modulePath)
    if 'description.html' in subdirs:
        return True
    else:
        return False
def getNamefromDescription(folderpath,module):
    descriptionFilePath = os.path.join(folderpath,module)
    soup = BeautifulSoup(open(descriptionFilePath),'html.parser')
    findtheH1=soup.find('h1')
    if findtheH1:
        name = str(findtheH1.getText()).strip('[]')
        return name

def writeModuleFoldersToDict(CMFolderPaths):
    #Open a csv file for writing. 
    #resultFiles = open("ModulesList.csv","w+")
    #resultFile.write("assetfolder,modulename,source,profiles/n")
    masterDict = {}
#For each folder path    
#Check that the folder is not empty, contains dirs
    print "writing Modules to Dictionary"
    CMFolderPaths = filter(notEmpty,CMFolderPaths)
#For remaining 'custom modules' folders, get the folder names inside them (module titles)
    for folderpath in CMFolderPaths:
#Lists out the module folders in a given 'custom modules' folder
        subdirs = os.listdir(folderpath)
        modulePaths = [folder for folder in subdirs if os.path.isdir(os.path.join(folderpath, folder))]
        modulesWithDescriptions = [module for module in modulePaths if hasDescription(folderpath, module)]
        print modulesWithDescriptions
#Upate the master dictionary with the folder name
        {masterDict.update({moduleName:[]}) for moduleName in modulePaths}
        #print folderpath, masterDict, '\n\n', len(masterDict)
#check if the asset folder name already in masterDict
#if its not, THEN check for a description.html
        modulesToGetName=[]
        for module in modulesWithDescriptions:
            if module not in masterDict.values():
                modulesToGetName.append(module)
        print modulesToGetName, 'get the names for these modules, please'

    print masterDict, len(masterDict)
    return masterDict

def getProfileName(autorunFilePath):
    
    theshortenedName = re.findall('(.*?\\\\)',autorunFilePath)
    return theshortenedName[-2][:-1] 


    #write each item in master dict as a line to the  csv file
    #return the final dictionary (Now you can start adding profiles in getProfiles()
def readAutorunMod(autorunPathList, masterDict):
    print autorunPathList, masterDict
    masterDictCopy = masterDict
    #iterates over all the autorun files we have paths for
    #This should get the modules called by that profile
    #zip them to a dict with names and profile
    #we have the masterDict
    #so given the names from the for loop below, shoudl append the profile name to all the module keys
    for autorunFile in autorunPathList:
        #get the profile name from the path by going two levels up.
        profilename = getProfileName(autorunFile)
        currentFile = open(autorunFile,"r")
        FiletoText = currentFile.read()
        modules = re.findall('(?=.*load)[^{]+{[^}]+}',FiletoText)[0]
        moduleLines = modules.split("\n")
        unwantedchars = {'load','{','}'}
        #Take off the leading whitespace
        moduleLines = [item[4:] for item in moduleLines if item not in unwantedchars]
        strippedModuleNames = []
        for x in moduleLines:
            theshortenedName = re.findall('(.*\/)',x)
            if theshortenedName:
                strippedModuleNames.append((theshortenedName[0])[:-1])
        strippedModuleNames = [item[1:] if item[0]=="*" else item for item in strippedModuleNames]
        print strippedModuleNames

        
#Combine [strippedModuleNames] and the [profile name] into a {dict} that can be matched to the {master dict} 
        for x in strippedModuleNames:
            masterDictCopy.setdefault(x, []).append(profilename)
                

   # for i in masterDictCopy:
        #print i, masterDictCopy[i],'\n'
    return masterDictCopy

    #print moduleLines
    #somefilepath=''
    #currentFile = open(somefilepath,"r")
   
def writeProfileFoldersToDict(profileFolderPaths):
    print "writing profile names to a dictionary"
    descriptionProfiles=[]
    for profileFolder in profileFolderPaths:
        directories = os.listdir(profileFolder)
        
#        modulesSubpath = os.path.join(profileFolder,"modules\autorun.mod")
#        modulesSubpathUpper = os.path.join(profileFolder,"Modules\autorun.mod")
        
        for givenDirectory in directories:
            modulesSubpath = os.path.join(profileFolder,givenDirectory,"modules\\autorun.mod")
            print modulesSubpath
            #modulesSubpathUpper = os.path.join(profileFolder,givenDirectory,"Modules\\autorun.mod")
            if os.path.exists(modulesSubpath):
                descriptionProfiles.append(modulesSubpath)
    return descriptionProfiles
"""
#Walk through bcb/Uniview and
#look for all folders called 'custom modules'
#Create [] of such folder paths 
#Should find all folders named 'custom_modules' 
"""

def findModuleFolders() :
    #NOTE: Change this to UniviewFolderPath='../../' for realimplementation
    UniviewFolderPath = '../../'
    HomePath = 'UVDatabase/scripts/'
    os.chdir(UniviewFolderPath)
    #directories = filter(os.path.isdir, os.listdir('.'))
    print "scanning for custom module and profiles folders now"
    allSubdirectories = os.walk(".", topdown=True)
    #print type(allSubdirectories)
    customModuleFolderPaths=[]
    profileFolderPaths=[]
    count=0
    for root, directories, files in allSubdirectories:
        for name in directories:
            if name.lower()=='custom modules':
                customModuleFolderPaths.append(os.path.join(root,name))
                print root, name
                count+=1
#Only testing over limited directories for now. bcb total scan takes too long
            if count==5:
                break
        if count==5:
            print "returned a list of  5 folders named 'custom modules'"
            #return customModuleFolderPaths
            break
    masterDict = writeModuleFoldersToDict(customModuleFolderPaths)

    count2=0
    for root, directories, files in allSubdirectories:
        for name in directories:
            if name.lower()=='profiles':
                profileFolderPaths.append(os.path.join(root,name))
                print name
                count2+=1
            if count2==10:
                break
        if count2==10:
            break
    print profileFolderPaths
#This gives us a list of folders that have an autorun.mod file
    foldersWithAutorun = writeProfileFoldersToDict(profileFolderPaths)
#Send [] and master {} to readAutorunMod([],{}) to get back a {} with profiles
    FinalDictionary = readAutorunMod(foldersWithAutorun, masterDict)
    print FinalDictionary
    os.chdir(HomePath)
    return FinalDictionary
    #a list of all folders with custom modules
    #print customModuleFolderPaths
    #a list of all folders name 'profiles'
    #print profileFolderPaths


