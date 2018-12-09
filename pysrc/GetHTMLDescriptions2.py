import os
from os import listdir
from os.path import isfile,join
import csv
from bs4 import BeautifulSoup
import pandas


def getDescriptionText():
    #with open("10pcdescription.html") as choice:
     #   firstsoup=BeautifulSoup(choice)
    soup = BeautifulSoup(open("10pcdescription.html"),'html.parser')
    findtheH1=soup.find('h1').getText()
    #findthep=soup.find('p').getText()
    #print findtheH1+ findthep
    print findtheH1
    
def getDescriptionTextSpecific(descriptionFilePath):
    #with open("10pcdescription.html") as choice:
     #   firstsoup=BeautifulSoup(choice)
    soup = BeautifulSoup(open(descriptionFilePath),'html.parser')
    findtheH1=soup.find('h1').getText()
    #findthep=soup.find('p').getText()
    #print findtheH1
    #print findthep
    result = str(findtheH1).strip('[]')
    return result
          
def getHTMLDescriptions():
    resultFile=open("HTMLDescriptionsList.txt","w+")
    #Put the headers in this write statement.
    #Right now the header entry will be dumb, only as user inputs
    #resultFile.write("assetname, module type, source, tags in array form\n")
    directories = filter(os.path.isdir, os.listdir('..\Custom Modules'))
    for item in directories:
        newLines= item+",,,[]\n"

    modulesWithDescriptions = []
    for item in directories:
        subDirPath = os.path.join(r'..\Custom Modules', item)
        subdir = os.listdir(subDirPath)
        for files in subdir:
            
            if files=="description.html":
                modulesWithDescriptions.append((os.path.join(subDirPath,"description.html")))
            
    resultFile.write("These are the module folders that have a description.html file \n")
    for eachline in modulesWithDescriptions:
        resultFile.write(eachline +'\n')
      #  print eachline
    resultFile.close()
    return modulesWithDescriptions
#TODO: A function that will get each module name with a description.html file
#And add the name to the module_name column in the csv file.

#This function returns all the asset folder names, ONLY the names, no paths
def onlyGetFolderName():
    directories = filter(os.path.isdir, os.listdir('..\Custom Modules'))
    #for item in directories:
    #    newLines= item+",,,[]\n"

    modulesWithDescriptions = []
    return directories

def onlyGetFoldersWithDescriptions():
    #List with all folders
    allFolders=onlyGetFolderName()
    #List with just folders that have descriptions
    modulesWithDescriptions=[]
    for item in allFolders:
        subDirPath = os.path.join(r'..\Custom Modules', item)
        subdir = os.listdir(subDirPath)
        for files in subdir:
            if files=="description.html":
                modulesWithDescriptions.append(item)
    #for j in modulesWithDescriptions:
     #   print j
    print modulesWithDescriptions
    return modulesWithDescriptions

def getTitlesFromDescriptions():
    #List of HTML description file paths
    ModuleNameList=[]
    DescriptionFilesList = getHTMLDescriptions()
    for i in DescriptionFilesList:
        currentline=getDescriptionTextSpecific(i)
        ModuleNameList.append(currentline)
    print ModuleNameList
    return ModuleNameList
      

#TODO: A function that takes the folder names and checks if they have a description.html
#Returns a 2d array with folder names and asset names
def linkFolderNametoAssetName():
    FolderNames=onlyGetFoldersWithDescriptions()
    print("breakbreak \n")
    ModuleNames=getTitlesFromDescriptions()
    mapped=zip(FolderNames,ModuleNames)
    print mapped
    return mapped

def addModuleNametoColumn():
    dataframe1=pandas.read_csv('CustomModulesList.csv')
    print dataframe1
    folderNames=dataframe1['asset folder']
    FolderNamesList=onlyGetFoldersWithDescriptions()
    LinkedList
    print folderNames
    for j in dataframe1['module name']:
        print j
        #list(modulesWithDescriptions)
    for k in folderNames:
        if (k in folderNamesList):
            

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

#pullTextTogether()
#addModuleNametoColumn()
#onlyGetFolderName()
linkFolderNametoAssetName()
addModuleNametoColumn()
