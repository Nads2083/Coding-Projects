 ** Be sure to review this ENTIRE document!

# Final Project
********************************
This project brings together the work you've done this semester into a single project. As we've discussed many times, Python is great for reporting large datasets. We'll be using a moderately sized dataset for our project.
Using what you've learned this semester, it's time to write a complete program, that is similar to that of a program you might be asked to write in the real world. You'll be responsible for writing the User Interface (UI) which displays on the screen, as well as generating reports as text files.  Your final submission will represent an example of a basic, fully functional, program that would be great for you to keep and refer to in job interviews.

For this project you will be writing a program that compares REAL mortality data gathered from the Centers For Disease Control. The data is publically available on the CDC website and is updated weekly.  We'll be specifically using the database maintained to report COVID deaths, as compared to other tracked mortality rates.  To keep things simple, this data is provided for you here in Repl as the following files:

#### FILES PROVIDED
  * cdc.csv - This report includes mortality data from the start date (shown in the file).  This file is "live", meaning it may update automatically from time to time during your project.  The format will not change, but the data on mortality could be updated to a more recent date and added to!

  * hints.md - Fairly obvious, I hope? 
#### --
## About Grading

Your program will be hand graded.  I will be reviewing quality and efficiency of code and comments as well as function.  The expectation is that this program will be clean, complete and fully debugged prior to submission.  However, I will consider applying partial credit in most cases, so be sure to submit your best effort.

 ** You must follow the following expectations for all project portions:
  * Program should end or quit ONLY when the user selects menu item 5. Exit
  * Make sure your program FULLY TESTS ALL USER INPUT.  
  * Be sure to handle any system errors, unless specifically directed not to.  I should see no "red" errors while testing your code.
  * Remember to BLOCK comment your code.  Failure to properly comment your code will result in a 0 for the project. 
  * Look closely at report names and headers.  Yours must match!  Reports should also include the timestamp (automatically generated) for when the report is written.  Be sure to see the hints for that code!

***
## Part I


Your program MUST effectively implement all of the following functions as described:

* main() - Void function.  Accepts nothing. Calls banner(). Calls the menu() and receives menu values. Loops, exits, and calls other functions as needed for each menu item.

* banner() - Void function. Accepts no input. Displays an ASCII banner for your project.

* menu() - Accepts nothing. Returns one integer. Asks the user to make a selection.  Tests selection to make sure it's a valid value.  Loops until a valid value is selected. For now, only items 1,2, and 5 need actions associated with them.  Returns an integer.

* openCDCfile() - Accepts nothing.  Opens the cdc.csv file, removes unneeded lines of data and returns the file handler (NOT the whole file as a string).  Hint: use next(fileHandler) to remove a line.

* defaultReport() - void function. This function must create a report called "Full_Mortality_By_State_Report.txt".  The report should closely resemble the example given below, with the same columns shown. The report must include ALL data (all dates) from the shown columns.  Remember that this file's data is based on weekly reports from the CDC. Thus it can, and may, be updated at anytime. How the goal of how displaying this data is achieved is left largely to the programmer. 

** Grading of this portion of the project will be based on efficiency of coding, quality of comments, and quality of report among other factors.

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
5. Exit

Make your selection from the menu: 
```

### Report File Example
```
National Mortality Rate by Cause Listed by State and Reporting Date Report    Sorted by State    
Report Generated: 11/08/2020     21:16:34
                              WEEK        TOTAL         NATURAL      C19 MULTIPLE    C19 UNDERLYING
STATE                         ENDING      DEATHS        CAUSES          CAUSES           CAUSE
--------------------------------------------------------------------------------------------------
Alabama                        1/5/19      1077            993              0              0
Alabama                       1/12/19      1090            994              0              0
Alabama                       1/19/19      1114           1042              0              0
Alabama                       1/26/19      1063            994              0              0
Alabama                        2/2/19      1095           1026              0              0
```

***
