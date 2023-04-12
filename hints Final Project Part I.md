***********************************
# HINTS:
************************************

## Code for inserting the current datetime. Just copy these three lines
```
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y     %H:%M:%S")
    f.write('\nReport Generated: '+dt_string+'\n')
```


## Pseudocode for my approach to main:
+ show the banner
+ show the menu, ask user to make a choice
   + Make sure choice is valid
+ if user choses a valid number, run that function.
  + if exit, then exit the logic block
+ Go back to begining


## Creating an ASCII Banner
Create the banner with a web program like:
[ASCII Banner Creator] (https://manytools.org/hacker-tools/ascii-banner/)
[Another ASCII Banner Creator] (http://www.patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)

Put the banner in triple quotes to show it correctly

