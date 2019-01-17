import os
from os import listdir
from os.path import isfile,join
import csv
import unittest
from bs4 import BeautifulSoup
import re

CustomModulesFolderPath = '..\..\custom modules'

#Generates a CSV table with the module names and empty columns otherwise
"""
def getCustomModulesList():
    resultFile=open("CustomModulesList.csv","w+")
    #Put the headers in this write statement.
    #Right now the header entry will be dumb, only as user inputs
    resultFile.write("asset folder,module name,source,profiles\n")
    directories = os.listdir(CustomModulesFolderPath)
    for item in directories:
        newLines= item+",,,[]\n"
        #print newLines
        resultFile.write(newLines)

    resultFile.close()
    print "A CSV table with 4 columns has been created.\n"
    print "You can find it in this directory as - CustomModulesList.csv\n"
"""
def notEmpty(aPath):
    return len(os.listdir(aPath))>0

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
    CMFolderPaths = filter(notEmpty,CMFolderPaths)
#For remaining 'custom modules' folders, get the folder names inside them (module titles)
    for folderpath in CMFolderPaths:
#Lists out the module folders in a given 'custom modules' folder
        subdirs = os.listdir(folderpath)
        modulePaths = [folder for folder in subdirs if os.path.isdir(os.path.join(folderpath, folder))]
        modulesWithDescriptions = [module for module in modulePaths if hasDescription(folderpath, module)]
        print modulesWithDescriptions
#Upate the master dictionary with the folder name
        {masterDict.update({moduleName:''}) for moduleName in modulePaths}
        #print folderpath, masterDict, '\n\n', len(masterDict)
#check if the asset folder name already in masterDict
#if its not, THEN check for a description.html
        modulesToGetName=[]
        for module in modulesWithDescriptions:
            if module not in masterDict.values():
                modulesToGetName.append(module)
        print modulesToGetName, 'get the names for these modules, please'

#I don't have the permissions to write/open files in this directory for some reason???
        #modulesToGetName=[getNamefromDescription(folderpath,item) for item in modulesToGetName]
        #print modulesToGetName, "These are the names from the description files"
    print masterDict, len(masterDict)
    return masterDict
    #write each item in master dict as a line to the  csv file
    #return the final dictionary (Now you can start adding profiles in getProfiles()
def readAutorunMod(autorunPathList, masterDict):
    print autorunPathList, masterDict
    for autorunFile in autorunPathList:
        currentFile = open(autorunFile,"r")
        FiletoText = currentFile.read()
        modules = re.findall('(?=.*load)[^{]+{[^}]+}',FiletoText)[0]
        moduleLines = modules.split("\n")
        unwantedchars = {'load','{','}'}
        moduleLines = [item[4:] for item in moduleLines if item not in unwantedchars]
    print moduleLines
    #somefilepath=''
    #currentFile = open(somefilepath,"r")
   
def writeProfileFoldersToDict(profileFolderPaths):
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
            #if os.path.exists(modulesSubpathUpper):
            #    descriptionProfiles.append(modulesSubpathUpper)
    print descriptionProfiles
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
    os.chdir(UniviewFolderPath)
    #directories = filter(os.path.isdir, os.listdir('.'))
    print "scanning for custom module and profiles folders now"
    allSubdirectories = os.walk(".", topdown=True)
    print type(allSubdirectories)
    customModuleFolderPaths=[]
    profileFolderPaths=[]
    count=0
    for root, directories, files in allSubdirectories:
        for name in directories:
            if name.lower()=='custom modules':
                customModuleFolderPaths.append(os.path.join(root,name))
                print root, name
                count+=1
#Only testing over 5 directories for now. bcb total scan takes too long
            if count==3:
                break
        if count==3:
            print "returned a list of  5 folders named 'custom modules'"
            #return customModuleFolderPaths
            break
    masterDict = writeModuleFoldersToDict(customModuleFolderPaths)

    count2=0
    for root, directories, files in allSubdirectories:
        for name in directories:
            if name.lower()=='profiles':
                profileFolderPaths.append(os.path.join(root,name))
                count2+=1
            if count2==3:
                break
        if count2==3:
            break
    print profileFolderPaths
#This gives us a list of folders that have an autorun.mod file
    foldersWithAutorun = writeProfileFoldersToDict(profileFolderPaths)
#Send [] and master {} to readAutorunMod([],{}) to get back a {} with profiles
    readAutorunMod(foldersWithAutorun, masterDict)
    #a list of all folders with custom modules
    #print customModuleFolderPaths
    #a list of all folders name 'profiles'
    #print profileFolderPaths
    

    #For each folder path in [],
    #Get the module folder name,
    #If it already exists, add the folder path to csv[folder path]
    #If it doesn't exist, create a new csv row and fill in csv[asset folder] and csv [folder path]

    #Check for modules with description.html
    #Strip the module name if available, add to csv column (matching by folder name as key)
findModuleFolders()
    

#Should get the profiles where modules were used.
#def getProfiles():
    #Walk through bcb/Uniview and
    #Look for folders named 'profiles'
    #Create [] of such folder paths + /././Modules/autorun.mod
    #For each in [], check that there is an autorun.mod file
    #map [] so that only folder paths w autorun.mod are remaining
    #Get the asset folder names from the autorun.mod files
    #check csv if module exists in csv[asset folde]
    #if exists, write to csv[profiles]
    #if does not exist, create a new line with the module name and csv[profiles]

#def csvtoJS():
    #Convert the final CSV to JavaScript Object and output to the screen. 
    
#Prints out the JS object, ready to be pasted into the index.html table
    #Might be able to just delete this
"""
def convertCSVtoJSFormat():
    result=[]
    with open("CustomModulesList.csv", "rb") as f:
        eachline='var dataSet = [';
        reader=csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            eachline+=str(line)+",\n"
            #print '{},'.format(line)
            #print eachline
        #remove the last comma
        eachline=eachline[:-2]
        #Add in a closing bracket for the dataset
        eachline+="]"
        print eachline
"""

