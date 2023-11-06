# HERE BE PERSONAL PROJECTS
## **Projects Include:**
### *Octopus Energy Cost*
Retrieves household electricity consumption for Octopus Energy Agile with 
half-hourly 
rates. These are multiplied together to get the cost and summed for the 
day's total cost. <br />
The data retrieved is uploaded to Google Sheets via Sheety.<br />
04/11/2023: Now with Cost per kWh column.<br />
05/11/2023: Update with columns for consumption rate, price, with cost per 
half hour segments. New sheet for November added. Automate month/year
for Sheety put hyperlink and json header.<br />
#### *TODO*
Possible  #TODO in future is to add user input to get product and tariff codes 
to user personal electricity rates and prices. <br />
Currently cannot add new sheet using the Sheety API. May require google API 
directly to create new sheets. Transfer of project to google API may be 
necessary. Or use selenium to automate new sheet creation as a 'simpler' 
workaround. <br />
For robustness, program should pull latest date reported on Google Sheets. 
This is so that in event of failure in data transfer, the missing rows can 
be added up to the current day.
-------------------------------------------------------------------------------
### *CS50 Final Project*
The project outlined in CS50p is left up to me to work through, with the 
minimum requirements of at least 3 functions in the code. Along my current 
interest in Critical Role, I chose to focus 
on a D&D dice roller that takes into account of a character's modifiers. 
The character can be created or can be retrieved from previously created 
using this script. <br />
#TODO is to finish the character saving and loading portion and other CS50
non-code related requirements.
-------------------------------------------------------------------------------
### *PDF Merger*
Simple pdf merger that I needed to merge train tickets together for ease of 
printing. Made to be somewhat user friendly.
-------------------------------------------------------------------------------