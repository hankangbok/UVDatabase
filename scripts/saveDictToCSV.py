import os
from os import listdir
from os.path import isfile,join
import csv
import pandas 
from GeneratesModulesListAutorun import master
#from CSVtoJs import convertCSVtoJSFormat

def saveDictToCSV():
    originalCSV = pandas.read_csv('CustomModulesList.csv')
    allcolumnnames = originalCSV.columns.tolist()
    howmanycolumns = len(allcolumnnames)
    blankLine = [""]*howmanycolumns

    #array of module names MASTER
    AssetFolder = originalCSV['asset folder']
    #array of profile names MASTER
    Profiles = originalCSV['profiles']
    #get the dictionary of module:[profiles] from the GeneratesModulesListAutorun python scan
    ProfilesDict = master()


    for key,value in ProfilesDict.iteritems():
        doeshave = AssetFolder[AssetFolder==key].empty
        if (doeshave==True):
            dictforDF = dict(zip(allcolumnnames, blankLine))        
            dictforDF['asset folder']=key
            dictforDF['profiles']=value
            originalCSV.loc[originalCSV.shape[0]+1]=dictforDF        
        else:
            currentIndex = AssetFolder.index[AssetFolder==key][0]
            
            originalCSV['profiles'][currentIndex]=value
    print "The CSV has been updated - check Final.csv in this directory"
    print "The profile column should now contain all profiles for which a given module has been used"

    originalCSV.to_csv('Final.csv', index =False)
    #print "\n\n\n\n\n"
    #convertCSVtoJSFormat()
    #convert to JS using the CSVtoJS Python script
