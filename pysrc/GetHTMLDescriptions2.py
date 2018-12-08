import os
from os import listdir
from os.path import isfile,join
import csv

from bs4 import BeautifulSoup

def getDescriptionText():
    #with open("10pcdescription.html") as choice:
     #   firstsoup=BeautifulSoup(choice)
    soup = BeautifulSoup(open("10pcdescription.html"),'html.parser')
    findtheH1=soup.find_all('h1')
    findthep=soup.find_all('p')
    print findtheH1+ findthep
def getDescriptionTextSpecific(descriptionFilePath):
    #with open("10pcdescription.html") as choice:
     #   firstsoup=BeautifulSoup(choice)
    soup = BeautifulSoup(open(descriptionFilePath),'html.parser')
    findtheH1=soup.find_all('h1')
    findthep=soup.find_all('p')
    print findtheH1
    print findthep
          
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
        print eachline
    resultFile.close()
    return modulesWithDescriptions
def pullTextTogether():
    DescriptionFilesList = getHTMLDescriptions()
    for i in DescriptionFilesList:
        getDescriptionTextSpecific(i)
#Use a function that will get the list of modules with description.html files
#That will then pass each file path as an argument to getDescriptionText
    #to get all the descriptions

pullTextTogether();
