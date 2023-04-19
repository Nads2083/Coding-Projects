# Mod 8.5: Advanced Reporting
- - - - 

## Directions for this Project ##
#### There is no test file for this project. It will be checked by hand. Do NOT submit this project unless you believe it runs fully and correctly. Submission of incomplete projects will not receive any points, but will waste the professor's time.  Please don't do that.

For this program, you're going to write several functions that work together to generate a text file report, and a visual update on the UI.
The program should work to append data from the report to a list, and then perform operations on that resulting list.

* main() - calls each of the other functions.
  - call readFile(), accept a file handler back to main
  - call reportAll, pass the file handler to reportAll.  Receive nothing back.
  - call readFile(), Pass nothing, receive file handler back.
  - call findHighTemp(), pass the file handler. Receive a string for date, and an integer for high temperature.
  - call printHighValues(), pass the date and temperature.

* readFile() open the 'ROAWeather.csv' file. Remove the header, return the file handler. 

* reportAll() Receive the file handler. Return nothing. Writes the data to a report called "WeatherOutput.txt"
  - open the file to be written.
  - loop through the file handler.
    - strip off newlines
    - replace quotes with zero length strings
    - replace commas with tabs
    - write the line
  - close the file after loops are finished
The report should be formatted as below.  Each line starts with "USW...". A line of data should not show on more than one line of output.  Be sure you add some sort of headers that describe the content of each column!
```
USW00013741 ROANOKE INTERNATIONAL AIRPORT    VA US  2020-11-06  0.00    74  43
USW00013741 ROANOKE INTERNATIONAL AIRPORT    VA US  2020-11-07  0.00    75  41
USW00013741 ROANOKE INTERNATIONAL AIRPORT    VA US  2020-11-08  0.00    75  46
USW00013741 ROANOKE INTERNATIONAL AIRPORT    VA US  2020-11-09  0.00    73  53
```

* findHighTemp() Receive file handler. Return integer of high temperature and string of date.
  - Create two empty lists, one for date strings, and one for temperature integers.
  - Loop through the file handler.
    - Replace the quotes with zero length strings
    - split the file on commas
    - append the HTEMP column values to one list.  The format for this is `mylist.append(data)`
    - append the DATE column values the second list. The format for this is `mylist.append(data)`
  - find the largest integer value in the temperature list. There is a function for this.
  - find the index of the largest integer value in the temperature list. The format for this is `mylist.index(list_object_to_be_indexed)`.
  - use the index of the largest integer to get the matching date in the date list
  - return the high temperature, and the correlated date string

* printHighValues() Receive the date string and temperature integer. Display on the screen a message similar to the following:
```
Full Report Posted
The highest temperature on record was set on 104. The date was 2012-06-29
```

