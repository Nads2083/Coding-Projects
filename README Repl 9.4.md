# Mod 7.4 Cleaning up the Output #
- - - - 

## Directions for this Project ##
 
For this exercise, you will write a program that pulls all of the email addresses from the headers.txt file that are preceeded with the sequence "Return-Path:" and display them in a list. You will show only the email address
Your output should include any duplicate entries found, but you do need to make sure it's only these specific addresses, and that there are no blank lines between entries.

You will create three functions that perform the following:
* main() opens the headers.txt file and passes it to showRecords. After the records are printed, main() catches the count of the records and passes that to userPrint().
* showRecords() this function receives the open file handler, and returns the count as an integer.  Be sure to do the following in this function:
  * loop through the file, replacing unneeded characters with zero length strings, and print each record required
  * count each record as it is printed
* userPrint() catches the count of the records and displays a message.

The last line of your report will state how many records were found

Make sure your output looks like mine, but be sure you've found ALL of the records (not just 3):
```
dr_bellomusa01@omaninfo.com
frankwilliams2@starmedia.com
lawrence.smith@voila.fr
Found 3 records.
```