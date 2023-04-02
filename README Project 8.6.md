# Mod 6.6 Project: String Triangle #
- - - - 

## Directions for this Project ##
 
Write a program that takes a string from the user, outputs it in a clever shape, and counts the number of characters printed to the screen.

This program must have the listed functions:  Failure to follow these requirements may result in a failing grade on the assignment even if it passes all tests: 

* main() Controls the flow of the program (calls the other modules).   
* userInput() Asks the user to enter a short sentence of *any* length. Return that sentence as a string.
* printTriangleUp() Accepts a string. Prints the sentence in a triangle from first letter to full sentence in the pattern as shown below. Counts the number of characters and returns the count as an integer. 
* printTriangleDown(): Accepts a string, and an integer. Prints the sentence in a triangle from full sentence to first letter in the pattern as shown below. Counts the number of characters and adds that number to the count from printTriangleUp().  Returns an integer of the count.
* countUsed(): Accepts one integer. prints out a message with the total count of letters printed.

I should see no "red" system errors while testing your code.

To pass the tests, you need to have your output look exactly like mine, but work with any string tested. It is not necessary to pass all of the included pytests for full credit:

Make sure your code looks like mine. I've given you two tests for this project, but sometimes it's hard to get them to pass.  I will HAND GRADE this project, so as long as it looks right, you're fine even if the tests fail:
```
Enter a short sentence: To be, or not to be? That should not be a question!

T
To
To 
To b
To be
To be,
To be, 
To be, o
To be, or
To be, or 
To be, or n
To be, or no
To be, or not
To be, or not 
To be, or not t
To be, or not to
To be, or not to 
To be, or not to b
To be, or not to be
To be, or not to be?
To be, or not to be? 
To be, or not to be? T
To be, or not to be? Th
To be, or not to be? Tha
To be, or not to be? That
To be, or not to be? That 
To be, or not to be? That s
To be, or not to be? That sh
To be, or not to be? That sho
To be, or not to be? That shou
To be, or not to be? That shoul
To be, or not to be? That should
To be, or not to be? That should 
To be, or not to be? That should n
To be, or not to be? That should no
To be, or not to be? That should not
To be, or not to be? That should not 
To be, or not to be? That should not b
To be, or not to be? That should not be
To be, or not to be? That should not be 
To be, or not to be? That should not be a
To be, or not to be? That should not be a 
To be, or not to be? That should not be a q
To be, or not to be? That should not be a qu
To be, or not to be? That should not be a que
To be, or not to be? That should not be a ques
To be, or not to be? That should not be a quest
To be, or not to be? That should not be a questi
To be, or not to be? That should not be a questio
To be, or not to be? That should not be a question
To be, or not to be? That should not be a question!
To be, or not to be? That should not be a question
To be, or not to be? That should not be a questio
To be, or not to be? That should not be a questi
To be, or not to be? That should not be a quest
To be, or not to be? That should not be a ques
To be, or not to be? That should not be a que
To be, or not to be? That should not be a qu
To be, or not to be? That should not be a q
To be, or not to be? That should not be a 
To be, or not to be? That should not be a
To be, or not to be? That should not be 
To be, or not to be? That should not be
To be, or not to be? That should not b
To be, or not to be? That should not 
To be, or not to be? That should not
To be, or not to be? That should no
To be, or not to be? That should n
To be, or not to be? That should 
To be, or not to be? That should
To be, or not to be? That shoul
To be, or not to be? That shou
To be, or not to be? That sho
To be, or not to be? That sh
To be, or not to be? That s
To be, or not to be? That 
To be, or not to be? That
To be, or not to be? Tha
To be, or not to be? Th
To be, or not to be? T
To be, or not to be? 
To be, or not to be?
To be, or not to be
To be, or not to b
To be, or not to 
To be, or not to
To be, or not t
To be, or not 
To be, or not
To be, or no
To be, or n
To be, or 
To be, or
To be, o
To be, 
To be,
To be
To b
To 
To
T

Total Count:  2601
```