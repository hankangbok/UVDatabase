from AssetFolderColumnGenerator import getCustomModulesList
from NameColumnGenerator import addModuleNametoColumn
from GeneratesModulesListAutorun import master
from saveDictToCSV import saveDictToCSV
from CSVtoJSfinal import convertCSVtoJSFormat
from CSVtoJSfinal import convertCSVtoJSFormatUsersChoice
from CSVtoJSfinal import convertCSVtoJSFormattoJSFile
import webbrowser
import os

def makeTableFromScratch():
    print ('file:///'+os.getcwd())[:-5]+'docs/index.html'
    #Output: CSV with BLANK  columns and asset folder populated column
    getCustomModulesList()
     #if successful:
    print "Table with 4 columns has been created"
    print "Scanning Uniview 2.0/Custom_Modules to get the names of the folders"
    print "[asset folders] aka column 1 has been populated\n"
    
    #Output: populates [module name] column for valid Custom modules
    addModuleNametoColumn()
    print "Scanning Uniview 2.0/Custom_Modules/<module names>/autorun.mod to strip out module titles"
    print "[module name] aka column 2 has been filled in\n"

    #Output: dictionary with [key:value] pairs where
    #key = module name, value = list of profiles utilizing said module.
    master()

    #Output: populates [profiles] column with profiles utilizing [module name]
    saveDictToCSV()
    print "Scanning Uniview 2.0/Profiles to get Uniview Profile Names"
    print "[profiles] aka column 4 has been filled in\n"

    #Output: Javascript object which allows webpage to display the updated table (../html/index.js)
    #Process: Converts the final csv table to a Javascript file, data is now reflected
    #on next webpage load.
    convertCSVtoJSFormattoJSFile()
    print "Reading Final.csv and converting to file index.js"
    print "index.js contains the DataTable object displayed by the webpage"
    print "This file will be located in the ../docs directory\n"

    #completed update, closing out program
    print "The local version of the website has been updated. \nOnce you exit, the updated webpage will open automatically. "
    toLeave = raw_input("Press any key to exit. ")

    #url = 'file:///C:/Users/hkang/SCISS/Uniview Theater 2.0/DatabaseCompiler_HK/html/index.html'
    
    url = ('file:///'+os.getcwd())[:-5]+'docs/index.html'
    print url
    webbrowser.open(url)

print "Is this folder saved to the correct location?\n (Should be: /Sciss/Uniview Theater 2.0/DatabaseCompiler_HK/pysrc) "
answer = raw_input("Please enter Y or N:" )
if (answer.lower()=="y"):
    print "\nDo you want this program to create a table for you?"
    if raw_input("Please enter Y or N: ").lower() == "y":
        print "\nAre you sure? Keep in mind that your previous Final.csv file will be overwritten completely.\n"
        if raw_input("Please enter Y or N: ").lower() == "y":
            makeTableFromScratch()
else:
    print "Please save the Database Compiler_HK folder in your /Uniview Theater 2.0 directory and try again. "

#ask if they're trying to make a table from scratch
