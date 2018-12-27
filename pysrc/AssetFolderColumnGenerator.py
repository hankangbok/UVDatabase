import os
from os import listdir
from os.path import isfile,join
import csv

CustomModulesFolderPath = '..\..\Custom Modules'

#Generates a CSV table with the module names and empty columns otherwise
def getCustomModulesList():
    resultFile=open("CustomModulesList.csv","w+")
    #Put the headers in this write statement.
    #Right now the header entry will be dumb, only as user inputs
    resultFile.write("asset folder,module name,source,profiles\n")
    directories = os.listdir(CustomModulesFolderPath)
    for item in directories:
        newLines= item+",,,[]\n"
        print newLines
        resultFile.write(newLines)

    resultFile.close()

#Prints out the JS object, ready to be pasted into the index.html table
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

getCustomModulesList()
convertCSVtoJSFormat()
