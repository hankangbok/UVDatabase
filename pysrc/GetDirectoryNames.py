import os
from os import listdir
from os.path import isfile,join
import csv

def getCustomModulesList():
    resultFile=open("CustomModulesList.csv","w+")
    #Put the headers in this write statement.
    #Right now the header entry will be dumb, only as user inputs
    resultFile.write("assetname, module type, source, tags in array form\n")
    directories = os.listdir('C:\Users\hkang\SCISS\Uniview Theater 2.0\Custom Modules')
    for item in directories:
        newLines= item+",,,[]\n"
        print newLines
        resultFile.write(newLines)

    resultFile.close()
    """
    for item in directories:
        subDirPath = os.path.join(r'C:\Users\hkang\SCISS\Uniview Theater 2.0\Custom Modules', item)
        print subDirPath + ' This is the subdirectory currently checking'
        subdir = os.listdir(subDirPath)
        for files in subdir:
            print files
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
        eachline=eachline[:-1]
        #Add in a closing bracket for the dataset
        eachline+="]"
        print eachline

getCustomModulesList()
convertCSVtoJSFormat()