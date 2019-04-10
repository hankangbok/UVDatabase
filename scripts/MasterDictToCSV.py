import os
from os import listdir
from ScanUniviewDir import findModuleFolders
import csv
import pandas
#receive the masterdict

#create a js file
def createJSFile():
    JSResult = open("DTSource.js", "w+")
    JSResult.write("This is a test")
    
def createCSVFile(dictionary):
    CSVResult = open("DTSource.CSV", "w")
    CSVResult.write("This is a test")
    CSVResult.write("asset folder,module name,source,profiles\n")
    for item in dictionary:
        currentLine = item+",,,"+dictionary[item]+"\n"
        CSVResult.write(currentLine)
    CSVResult.close()
    print "A CSV table with 4 columns has been created. \n"
    print "You can find it in this directory as 'DTSource.csv'"
#make a table with x number of columns
#write module names, profiles to the dictionary. Thats two columns down

#future columns will have to take the [asset folder] column and convert that to a dict key list. 



#make a blank csv with
#column headers
#module names only
def createCSV(dictionary):
    print "creating csv"
    resultCSV = open("initialize.csv","w+")
    headers = "module folder name,modulename,source,profiles,blank"+"\n"
    resultCSV.write(headers)
    #add in the module names with the module-profiles dictionary
    moduleNames = list(dictionary.keys())
    for name in moduleNames:
        resultCSV.write(name+str(',')*(len(headers.split(','))-2)+'[],\n')
    resultCSV.close()


#Generate dictionary for:
#Profiles DONE
#Module folder path TODO
#Module names TODO 

#Take a dictionary of module-variable pairs and match to columns in the csv
#Check if column header exists
#match key to column with pandas
#get columns
#append values
#write to CSV
def addColumnDictToCSV(dictionary, columnName):
    originalCSV = pandas.read_csv('initialize.csv')
    allcolumnnames = originalCSV.columns.tolist()
    blankLine = [""]*len(allcolumnnames)
    moduleNames = originalCSV['module folder name']
    newColumn = originalCSV[columnName]
    
    newLine = dict(zip(allcolumnnames, blankLine))
    print newLine, "this is what a blank line should be like"
    if columnName in originalCSV:
        for key, value in dictionary.iteritems():
            print key
            moduleExistsInCSV = moduleNames[moduleNames==key].empty
            #confusing syntax, but if module does NOT exist in csv, adds it to the csv as a new line
            if moduleExistsInCSV==True:
                newLine = dict(zip(allcolumnnames, blankLine))
                #print newLine
                newLine['module folder name'] = key
                newLine[columnName] = value
                originalCSV.loc[originalCSV.shape[0]+1]=newLine        
            #if module already exists in csv, append the profile name to the profile column 
            else:
                currentIndex = moduleNames.index[moduleNames==key][0]
                originalCSV[columnName][currentIndex]=value
    originalCSV.to_csv('initialize.csv',index=False)



#convertCSVtoJSFormattoJSFile()
#Take the final csv and convert to a js file ready to use
def convertCSVtoJSFile():
    result=[]
    with open("initialize.csv", "rb") as f:
        eachline='var dataSet = [';
        reader=csv.reader(f, delimiter=",")
        for i, line in enumerate(reader,1):
            eachline+=str(line)+",\n"
            #print '{},'.format(line)
            #print eachline
        #remove the last comma
        eachline=eachline[:-2]
        #Add in a closing bracket for the dataset
        eachline+="];"
        eachline+="""$(document).ready(function() {
			$('#example').DataTable( {
				mark:true,
				autoWidth:false,
				data: dataSet,
				"pageLength":30,
				columns: [
					{ title: "Asset Folder"},
					{ title: "Module Name" },
					{ title: "Date of Creation" },
					{ title: "Profiles"}

				],
				           columnDefs: [
                {
                    render: function (data, type, full, meta) {
                        return "<div class='text-wrap width-200'>" + data + "</div>";
                    },
                    targets: 3
                }
             ]
			} );
			$.extend(true, $.fn.dataTable.defaults, {
				mark: true
			});
			$('div.dataTables_filter input').focus();

		});"""
        #print eachline
    finalIndexJS=open("../docs/masterTest.js","w+")
    finalIndexJS.write(eachline)
    finalIndexJS.close()

"""
Might be able to delete this
"""
def createCSVLines(dictionary):
    finalText = "asset folder,module name,source,profiles\n"
    for item in dictionary:
        currentLine = str(item)+",,,"+str(dictionary[item])+"\n"
        finalText+=currentLine
    print finalText
    return finalText

def convertCSVtoJSFormat(dictionary):
   finalText=''
   finalText+="var dataSet = [['asset folder','module name','source','profiles'],\n"
   for item in dictionary:
       currentLine = "['"+str(item)+"'"+',"","","'+str(dictionary[item])+'"],\n'
       finalText+=currentLine
   finalText=finalText[:-2]
   finalText+="];\n"
   finalText+="""$(document).ready(function() {
			$('#example').DataTable( {
				mark:true,
				autoWidth:false,
				data: dataSet,
				"pageLength":30,
				columns: [
					{ title: "Asset Folder"},
					{ title: "Module Name" },
					{ title: "Date of Creation" },
					{ title: "Profiles"}

				],
				           columnDefs: [
                {
                    render: function (data, type, full, meta) {
                        return "<div class='text-wrap width-200'>" + data + "</div>";
                    },
                    targets: 3
                }
             ]
			} );
			$.extend(true, $.fn.dataTable.defaults, {
				mark: true
			});
			$('div.dataTables_filter input').focus();

		});"""
   print finalText


dictionary = findModuleFolders()
createCSV(dictionary)                                    

addColumnDictToCSV(dictionary, 'profiles')
convertCSVtoJSFile()
#convertCSVtoJSFormat(dictionary)
#createCSVLines(dictionary)

