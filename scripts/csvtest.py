import os
from os import listdir
from ScanUniviewDir import findModuleFolders
#receive the masterdict

#create a js file
def createJSFile():
    JSResult = open("DTSource.js", "w+")
    JSResult.write("This is a test#2")
#create a csv file (need to check if this works, since I've had issues with bcb permissions
def createCSVFile(dictionary):
    CSVResult = open("DTSource.csv", "w+")
    CSVResult.write("This is a test")
    CSVResult.write("asset folder,module name,source,profiles\n")
    for item in dictionary:
        print item
        currentLine = str(item)+",,,"+str(dictionary[item])+"\n"
        CSVResult.write(currentLine)
    CSVResult.close()
    print "A CSV table with 4 columns has been created. \n"
    print "You can find it in this directory as 'DTSource.csv'"

def createCSVFileSimple():
    testLine = "HAHAHAHAA"
    CSVResult = open("DTSource.CSV", "w+")
    CSVResult.write("This is a test")
    CSVResult.write("asset folder,module name,source,profiles\n")
    CSVResult.write(testLine)
    CSVResult.close()
    print "A CSV table with 4 columns has been created. \n"
    print "You can find it in this directory as 'DTSource.csv'"
dictionary = findModuleFolders()

#createJSFile()
createCSVFile(dictionary)
#createCSVFileSimple()
