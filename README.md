# Uniview Assets Library
## Test Deployment live at: 
https://kyouyatamax.github.io/UVDatabase/
## How to Use:
- Search for an asset by keyword using the Search bar at the top left
- Sift manually through the list of assets using the page numbers at the bottom of the page
- Toggle the number of entries displayed per page.

## Description: A database of Uniview Assets.
This database will ultimately be based off of a .csv file.   
The custom_modules.csv file will be converted into a Javascript array of objects, and formatted into a table. By using the [DataTables] (https://datatables.net/) Plugin for JQuery, the resulting table will be searchable.  

  
## Future Features: 
(Hoo boy there's a lot):
- Data entry can be done within Excel to speed things up.
- CAUTION: the csv file must always be saved as a csv file, not .xlsx or .xlx. 
- <b>Clean up the file structure</b>: right now, the files are jumbled up into the html file. This must be corrected.
- Build test cases (missing values, undefined, large values, missing columns, etc.)  
- Make it <b>pretty (CSS code</b>, right now this is dependent on the css code recommended by the DataTables Plugin).   
- Add a <b>Javascript form</b> to the page so that users can enter data for new assets. 
- Data Entry for the actual csv base file. 

## NOTE:
Right now, this webpage is just an html page with no backend.
Eventually, I want to migrate this to webpack and make the functions more modular. Just nicer. For now, I'm just trying to get things to work at least a little bit.    

## Technologies Used: 
- [DataTables] (https://datatables.net/) Plugin for JQuery  
- [JQuery] (Link Needed) 
- Javascript
- HTML
- CSS
- Flexbox (Eventually)


### Why DataTable?
1) I figured it would be nice if this were a webpage that PL staff could access (I don't think there's any sensitive information included)
2) Excel is nice, but using find/find all every time I want to look for something seemed a little tiresome. 
