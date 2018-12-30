import csv
def convertCSVtoJSFormat():
    result=[]
    with open("Final.csv", "rb") as f:
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
        #print eachline

def convertCSVtoJSFormatUsersChoice():
    result=[]
    chosenCSV=raw_input("Please enter the name of the CSV table you want to use to update the webpage.")
#eventually add regex to ensure that only valid .csv file names are entered
    with open(chosenCSV, "rb") as f:
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
        #print eachline

def convertCSVtoJSFormattoJSFile():
    result=[]
    with open("Final.csv", "rb") as f:
        eachline='var dataSet = [';
        reader=csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
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
    finalIndexJS=open("../html/master.js","w+")
    finalIndexJS.write(eachline)
    finalIndexJS.close()
