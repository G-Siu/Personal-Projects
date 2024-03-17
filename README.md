# HERE BE PERSONAL PROJECTS
## **Projects Include:**
<div style="text-align: justify">

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
### *Last Day of Month*
Function to check if current day is last day of the month.<br />
17/03/2024: Created.
#### *TODO*
Possible TODO in future is to add user input to get product and tariff codes 
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
Limitations include:
- Not accounting proficiencies such as Rogue Expertise
- Cannot roll different die faces at same time
- Requires manually stating ability checks

~~TODO is to finish the character saving and loading portion and other CS50
non-code related requirements.~~ <br />
The ability to save and load a character is now available and functional. 
<br />
TODO make code more robust as only partially filters out user typing errors.
<br />
TODO should produce user-friendly prompts, such as race stats should be 
displayed during character creation.
-------------------------------------------------------------------------------
### *PDF Merger*
Simple pdf merger that I needed to merge train tickets together for ease of 
printing. Made to be somewhat user friendly.
-------------------------------------------------------------------------------
### *Colour Detect*
Detect RGB colour palette at mouse pointer (rather inelegantly). Found on 
Stack Overflow, modified with a delay, so it doesn't continuously print. 
Requires the 'pyautogui' package.
-------------------------------------------------------------------------------
### *J's DnD Sessions*
A reason to practice writing in markdown in context of summarising a 
friend's DnD sessions. This includes summaries of each session, AI 
generated pictures of characters, etc. All content belongs to said friend 
and DnD group.<br />
Within this project, I wrote a Python script to automatically convert the 
party's names in the Markdown document with colour for ease of reading. I 
learned that Markdown syntax does not support colour, which led to the use 
of HTML markup instead.
-------------------------------------------------------------------------------
### *Date Difference*
Misunderstood assignment and created a date difference program that can calculate the difference between two dates by days. Super simple.
-------------------------------------------------------------------------------
</div>