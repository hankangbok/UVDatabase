import os
from os import listdir
from ScanUniviewDir import findModuleFolders
#receive the masterdict

#create a js file
def createJSFile():
    JSResult = open("DTSource.js", "w+")
    JSResult.write("This is a test")
#create a csv file (need to check if this works, since I've had issues with bcb permissions
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

dictionary = findModuleFolders()
#createJSFile()
#createCSVFile(dictionary)
#Okay, it really won't let me write to the csv or js files
#lets see if I can make a printed output that works if I paste it into the js file.
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

#createCSVLines(dictionary)
convertCSVtoJSFormat(dictionary)
