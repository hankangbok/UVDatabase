from AssetFolderColumnGenerator import getCustomModulesList
from NameColumnGenerator import addModuleNametoColumn
from GeneratesModulesListAutorun import master
from saveDictToCSV import saveDictToCSV
from CSVtoJSfinal import convertCSVtoJSFormat
from CSVtoJSfinal import convertCSVtoJSFormatUsersChoice
from CSVtoJSfinal import convertCSVtoJSFormattoJSFile

#AssetFolderColumnGenerator
#Generate Original CSV with some number of columns
#Fill Original CSV with asset folder names (col 1)
#These are from scanning over the Custom_Modules Folder
getCustomModulesList()


#nameColumnGenerator.py
#read in original CSV
#get the asset folder column
#get the module name column
#get [] with description.html
#zip the two together into [] of valid module-title pairs
#get each asset folder name, match to column in original CSV
#add the module title to the module name column of original csv
#CHANGE DATAFRAME1.TO_CSV so that it writes to the same file.
addModuleNametoColumn()



#generateModulesListAutorun.py
#scan profiles foler to get [] of profiles with an autorun.mod file
#scan each autorun.mod file to get [] of modules used in the profile
#construct dict {module name: profile} where keys are module names, profile names are values
master()

#saveDictToCSV
#Import CSV
#get module names column
#get profile names column
#match the module names to the profile names [if !module name in column, add a new entry]
#Push into a csv file
saveDictToCSV()

#convert it to js
#update the index.js file
convertCSVtoJSFormattoJSFile()
#convertCSVtoJSFormatUsersChoice()
#completed update
toLeave = raw_input("Your html is updated with the latest results from scanning your Univew Directory. Press any key to exit. ")
