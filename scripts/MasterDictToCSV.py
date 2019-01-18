import os
from os import listdir

#receive the masterdict

#create a js file
def createJSFile():
    JSResult = open("DTSource.js", "w+")
    JSResult.write("This is a test")
#create a csv file (need to check if this works, since I've had issues with bcb permissions
def createCSVFile():
    CSVResult = open("DTSource.CSV", "w+")
    CSVResult.write("This is a test")
#make a table with x number of columns
#write module names, profiles to the dictionary. Thats two columns down

#future columns will have to take the [asset folder] column and convert that to a dict key list. 


createJSFile()
createCSVFile()
