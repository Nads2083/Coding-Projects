 ** Be sure to review this ENTIRE document!

# Final Project
********************************

*** 
## Part II
All of the functionality of your project part 1 must be maintained.  Everything in part 2 is an update and/or addition to that existing program!

#### Creating Comparison Reports

* menu() - Gets an update: Updates the UI with a new menu option for "5. Highest COVID mortality Week"
Accepts nothing. Returns one integer. Asks the user to make a selection.  Tests selection to make sure it's a valid value.  Loops until a valid value is selected.  Returns an integer.

* getUserInputDates() accepts nothing. Calls getAvailableDates and displays the earliest and latest date of the cdc.csv file for the user. Asks user for start and end dates for the report. Gives the option of automatically setting start and end dates with the letter 'S' and 'E' (see output example). This function requires user to enter a valid start and end date (IE: dates covered in the data) in that order. Start and end date input requests must repeat individually until this is accomplished for both. Use the provided convertDate() function to temporarily convert strings to date objects for comparison. Returns a valid start and end date as strings (NOT as date objects)  

* getAvailableDates() accepts nothing. Calls openCDCFile() and determines the first date and the last date available in the document. Remember that this document is NOT in date order, so you cannot assume the first line is the first date and the last line is the last date. This file may also be updated at anytime, so be sure you're always reviewing the most up to date data.  Returns two strings: the start date, and the end date, in that order.

* reportSingleStateDataByDate() accepts nothing. This function is very similar to the default report. However, it reports for a single, user selected state and for a specific, user defined date range.  Ask the user to enter a State to review. Assume the user will enter a valid state name (I will not test this with invalid State names). Call getUserInputDates() to get a date range for the function. Using this State and date range, generate a report file called "Mortality_For_State_By_Date_Range_Report.txt". The report should closely resemble the example given below. The report must include ALL data from the cdc.csv file for the selected State and date range.  Remember that this file's data is based on weekly reports from the CDC. Thus it can, and may, be updated at anytime. How this goal is achieved is left largely to the programmer. 

* totalMortalityByState() accepts nothing. This function generates a report of the sum total of deaths, as well as the total of those were natural causes, C19 Multiple Causes, and C19 Underlying Cause for the entire date range. This function creates a report file called report called "Mortality_Summary_For_All_States_By_Date_Range_Report.txt".  It then prints the headers, and loops through the data to generate each total. This function doesn't write the line details though.
Once the total numbers are determined for a State, the state name, and the four total value integers are sent to printLineDetailReport() to be printed to the report.

* printLineDetailReport() receives the open file handler, the State, and four integers (in THAT order) which represent the sum for each State: Total Deaths, Natural Causes, C19 Multiple Causes, and C19 Underlying Causes.  Converts the integers to strings, then appends the summary detail to the report "Mortality_Summary_For_All_States_By_Date_Range_Report.txt". 

* getHighestMortality() Accepts nothing. This function must determine the highest reported week of COVID19 mortality as an underlying cause of death, what week that was, what state (or report location) it occured in, and what percentage of total deaths that week this number represents.  The function then prints out the message on screen as shown at the end of this readme file.


** Grading of this portion of the project will be based on proper implementation of each function, efficiency of coding, quality of comments, and quality of report among other factors. 

### UI Example
```
_____________________________________________________ 
╔═╗┬┌┐┌┌─┐┬    ╔═╗┬─┐┌─┐ ┬┌─┐┌─┐┌┬┐  ┌─┐┬─┐  ╔╦╗╦╔═╗┬
╠╣ ││││├─┤│    ╠═╝├┬┘│ │ │├┤ │   │   │ │├┬┘   ║║║║╣ │
╚  ┴┘└┘┴ ┴┴─┘  ╩  ┴└─└─┘└┘└─┘└─┘ ┴   └─┘┴└─  ═╩╝╩╚═╝o 
_____________________________________________________ 
 

Mortality Rate Comparison Menu
    
1. Show This Menu Again
2. Full Mortality Report by State
3. Mortality for a Single State, by Date Range
4. Mortality Summary for all States
5. Highest COVID mortality Week
6. Exit

Make your selection from the menu: 3
What State do you want to review? Virginia
Reporting is available from 1/5/19 to 10/24/20
Choose your starting date in (mm/dd/yyyy) format, or S for the first date of the data: 08/1/2020
Select your ending date in (mm/dd/yyyy) format or E for the last date of the data: 8/1/20
Not a valid date or format. Please try again.
Select your ending date in (mm/dd/yyyy) format or E for the last date of the data: e


**** REPORT PRINTED **** 
```

### Mortality for State By Date Range Report
```
Mortality for Virginia, by Date Range    For the selected date range 08/1/20 - 10/24/20

Report Generated: 11/08/2020     21:12:51

              WEEK        TOTAL         NATURAL      C19 MULTIPLE    C19 UNDERLYING
STATE        ENDING      DEATHS        CAUSES          CAUSES           CAUSE
-------------------------------------------------------------------------------------
Virginia     8/1/20      1452           1326            102             97
Virginia     8/8/20      1505           1367             87             83
Virginia    8/15/20      1448           1361            101             89
Virginia    8/22/20      1449           1357            123            113
```

### Mortality Summary for All States Report
```
Mortality Summary For All States By Date Range Report
For the selected date range 1/5/19 - 10/24/20

Report Generated: 11/08/2020     21:20:11

               TOTAL    NATURAL       C19 MULTIPLE    C19 UNDERLYING
STATE          DEATHS   CAUSES          CAUSES           CAUSE
--------------------------------------------------------------------
Alabama       101510     93994           3838           3838
Alaska          8142      6793              0              0
Arizona       121413    108669           5278           5278
```

### Highest Mortality Week Report

```
_____________________________________________________ 
╔═╗┬┌┐┌┌─┐┬    ╔═╗┬─┐┌─┐ ┬┌─┐┌─┐┌┬┐  ┌─┐┬─┐  ╔╦╗╦╔═╗┬
╠╣ ││││├─┤│    ╠═╝├┬┘│ │ │├┤ │   │   │ │├┬┘   ║║║║╣ │
╚  ┴┘└┘┴ ┴┴─┘  ╩  ┴└─└─┘└┘└─┘└─┘ ┴   └─┘┴└─  ═╩╝╩╚═╝o 
_____________________________________________________ 
 

Mortality Rate Comparison Menu
    
1. Show This Menu Again
2. Full Mortality Report by State
3. Mortality for a Single State, by Date Range
4. Mortality Summary for all States
5. Highest COVID mortality Week
6. Exit

Make your selection from the menu: 5


The largest number of deaths directly attributible to COVID 19 in this report range was 7200 in Texas during the week of 01/01/01.

This represents 3% of the total reported deaths in Texas that week.


```
** Because there seems to always be one person that wants to nitpick:**
+ By State, I mean States, Commonwealths, US properties, Cities, and whatever other types of communities that appear in the CDC.csv file

**Information used in UI Examples is NOT Valid data, but just example data. Your reports should have valid data.**