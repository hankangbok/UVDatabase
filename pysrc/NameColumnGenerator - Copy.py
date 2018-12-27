import os
from os import listdir
from os.path import isfile,join
import csv
from bs4 import BeautifulSoup
import pandas


CustomModulesFolderPath = '..\..\Custom Modules'

#given the filepath of a modules description.html file,
#return the title of the module as a string
def getDescriptionTextSpecific(descriptionFilePath):
    soup = BeautifulSoup(open(descriptionFilePath),'html.parser')
    findtheH1=soup.find('h1').getText()
    result = str(findtheH1).strip('[]')
    return result

#Searches /Custom_Modules for modules which have a description.html file
#Writes a list of such valid modules to 'ModuleswithdescriptionsList.txt"
#Returns a list of such valid modules
def getHTMLDescriptions():
    resultFile=open("ModuleswithdescriptionsList.txt","w+")
    directories = os.listdir(CustomModulesFolderPath)
    #directories = filter(os.path.isdir, os.listdir(CustomModulesFolderPath))
    for item in directories:
        newLines= item+",,,[]\n"

    modulesWithDescriptions = []
    for item in directories:
        subDirPath = os.path.join(CustomModulesFolderPath, item)
        subdir = os.listdir(subDirPath)
        for files in subdir:
            if files=="description.html":
                modulesWithDescriptions.append((os.path.join(subDirPath,"description.html")))            
    resultFile.write("These are the module folders that have a description.html file \n")
    for eachline in modulesWithDescriptions:
        resultFile.write(eachline +'\n')
    resultFile.close()
    #print modulesWithDescriptions
    return modulesWithDescriptions

#Returns a list of asset folder names, without filepaths
def onlyGetFolderName():
    #directories = filter(os.path.isdir, os.listdir(CustomModulesFolderPath))
    directories = os.listdir(CustomModulesFolderPath)

    #modulesWithDescriptions = []
    return directories

#Returns list of only modules which have description files
def onlyGetFoldersWithDescriptions():
    allFolders=onlyGetFolderName()
    modulesWithDescriptions=[]
    for item in allFolders:
#        subDirPath = os.path.join(r'..\Custom Modules', item)
        subDirPath = os.path.join(CustomModulesFolderPath, item)

        subdir = os.listdir(subDirPath)
        for files in subdir:
            if files=="description.html":
                modulesWithDescriptions.append(item)

    #print modulesWithDescriptions
    return modulesWithDescriptions

def getTitlesFromDescriptions():
    #List of HTML description file paths
    ModuleNameList=[]
    DescriptionFilesList = getHTMLDescriptions()
    for i in DescriptionFilesList:
        currentline=getDescriptionTextSpecific(i)
        ModuleNameList.append(currentline)
    #print ModuleNameList
    return ModuleNameList
      

#TODO: A function that takes the folder names and checks if they have a description.html
#Returns a 2d array with folder names and asset names
def linkFolderNametoAssetName():
    FolderNames=onlyGetFoldersWithDescriptions()
    print("breakbreak \n")
    ModuleNames=getTitlesFromDescriptions()
    mapped=zip(FolderNames,ModuleNames)
    #print mapped
    return mapped

def addModuleNametoColumn():
    dataframe1=pandas.read_csv('CustomModulesList.csv')
    print dataframe1
    folderNames=dataframe1['asset folder']
    moduleNamesCSV=dataframe1['module name']
    
    FolderNamesList=onlyGetFoldersWithDescriptions()
    linkedFolderNameList = linkFolderNametoAssetName()
    #print linkedFolderNameList
#    print folderNames
    for i in linkedFolderNameList:
        currentAssettoMatch = i[0]
        #print currentAssettoMatch
        linkedModuleName = i[1]
        insertIndex=folderNames[folderNames==currentAssettoMatch].index[0]
        #print insertIndex
        #insertIndex = folderNames.index(currentAssettoMatch)
        #print insertIndex
        moduleNamesCSV[insertIndex] = linkedModuleName    
    dataframe1['module name'] = moduleNamesCSV
    dataframe1.to_csv('Custom_updated.csv',index=False)
           

def pullTextTogether():
    DescriptionFilesList = getHTMLDescriptions()
    HTMLDescriptionText=open("HTMLDescriptionText.txt", "w+")
    for i in DescriptionFilesList:
        currentline=getDescriptionTextSpecific(i)
        HTMLDescriptionText.write(currentline+'\n')
    HTMLDescriptionText.close()
#Use a function that will get the list of modules with description.html files
#That will then pass each file path as an argument to getDescriptionText
    #to get all the descriptions

linkFolderNametoAssetName()
addModuleNametoColumn()
