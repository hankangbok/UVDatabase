import os
from os import listdir
from os.path import isfile,join
import csv
import unittest

CustomModulesFolderPath = '..\..\custom modules'

#Generates a CSV table with the module names and empty columns otherwise
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
def notEmpty(aPath):
    return len(os.listdir(aPath))>0

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
        #modulePaths = filter(os.path.isdir(os.path.join(folderpath,x)), os.listdir(folderpath))
        print modulePaths
#Upate the master dictionary with the folder name
        {masterDict.update({moduleName:''}) for moduleName in modulePaths}
        print folderpath, masterDict, '\n\n', len(masterDict)

    #write each item in master dict as a line to the  csv file
    #return the final dictionary (Now you can start adding profiles in getProfiles()
    
#Should find all folders named 'custom_modules' 
def findModuleFolders() :
    #NOTE: Change this to UniviewFolderPath='../../' for real implementation
    UniviewFolderPath = '../../'
    os.chdir(UniviewFolderPath)
    #directories = filter(os.path.isdir, os.listdir('.'))
    print "scanning for custom module and profiles folders now"
    allSubdirectories = os.walk(".", topdown=True)
    print type(allSubdirectories)
    customModuleFolderPaths=[]
    profileFolderPaths=[]
    finalcount = 100
    count=0
    for root, directories, files in allSubdirectories:
        for name in directories:
            if name.lower()=='custom modules':
                customModuleFolderPaths.append(os.path.join(root,name))
                print root, name
                count+=1
            if count==finalcount:
                break
        if count==finalcount:
            print "returned a list of  5 folders named 'custom modules'"
            #return customModuleFolderPaths
            break
    writeModuleFoldersToDict(customModuleFolderPaths)
    #i=0
    #while i<5:
    #    print allSubdirectories[1][i]
    #    i+=1

    #for root, directories, files in allSubdirectories:
        #print something
        #for name in directories:
            #if name.lower()=='custom modules':
            #    customModuleFolderPaths.append(os.path.join(root,name))
            #    print os.path.join(root,name)
            #if name.lower()=='profiles':
            #    profileFolderPaths.append(os.path.join(root,name))
            #    print root
    #a list of all folders with custom modules
    print customModuleFolderPaths
    #a list of all folders name 'profiles'
    print profileFolderPaths
    
    #Walk through bcb/Uniview and
    #look for all folders called 'custom modules'
    #Create [] of such folder paths

    #For each folder path in [],
    #Get the module folder name,
    #If it already exists, add the folder path to csv[folder path]
    #If it doesn't exist, create a new csv row and fill in csv[asset folder] and csv [folder path]

    #Check for modules with description.html
    #Strip the module name if available, add to csv column (matching by folder name as key)
#findModuleFolders()
    

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

