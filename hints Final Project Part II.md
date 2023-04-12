***********************************
# HINTS:
************************************

## Code for inserting the current datetime. Just copy these three lines
```
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y     %H:%M:%S")
    f.write('\nReport Generated: '+dt_string+'\n')
```

## Functions that have been created for you:

removeSpace() - Accepts a string.  Returns an int.  If string is empty, a integer of zero is returned.

convertDate(dateString) - Accepts a string.  Returns a date object.

## Pseudocode for my approach to main:
show the banner
show the menu, ask user to make a choice
   Make sure choice is valid
if user choses a valid number, run that function or exit.
Go back to begining


## Creating an ASCII Banner
Create the banner with a web program like:
[ASCII Banner Creator] (https://manytools.org/hacker-tools/ascii-banner/)
[Another ASCII Banner Creator] (http://www.patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)

Put the banner in triple quotes to show it correctly

## Rough Flowcharts for select functions:
Keep in mind that my charts are MY way of thinking when I plan out a program like you've been assigned. These are provided without warranty or promise of usefulness!

defautReport-flowchart.png)
totalMortalityByState-flowchart.png)

## Coding thoughts
Once you've figured out how to open and format a file, you'll probably use similar code for all of your reporting functions. Depending on your approach, it's probably only necessary to append values to a file for the getHighestMortality() function.