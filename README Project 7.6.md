*Remember that this is a project, so it is fully graded by your professor! The tests included in this project are to help you know if your project runs, but do not necessarily test all requirements.  Be sure you fully test your own code before submitting it!*

It is strongly recommended that you run pytest in the shell!


Be sure to fully comment your code.  Incomplete or missing comments will result in a 0 for the project and an Academic Honesty review.  Misspellings in code may result in significant point loss.

This program must have 11 functions: Failure to follow these requirements may result in a failing grade on the assignment even if it passes all tests: 


* main() Controls the flow of the program (calls the other modules). This includes decision logic (such as while True, if/elif/else) to call functions as requested. 
* userMenu() Displays choices.
* userInput() Asks the user to select a menu option. If any menu item is selected, ask to enter two numbers. Hint: Don't cast the input to number types. Let inputTest() do that.
* inputTest() Accepts one value from userInput(). Tests value to make sure it's a number. If it's not a number, it will ask for a valid number. This is one of the few times you can have a user input values in a function other than "userInput(). Returns valid numbers.
* add() Accepts two numbers, returns the sum
* subtract() Accepts two numbers, returns the difference of the first number minus the second number
* multiply() Accepts two numbers, returns the product
* divide() Accepts two numbers, returns the quotient of the first number divided by the second number
* modulo() Accepts two numbers, returns the modulo of the first number divided by the second number
* exponent() Accepts two numbers, returns the first number raised to the power of the second number.
* userOutput() Gives a user friendly output of the selected calculation. HINT: make your code reusable so that this method contains no decision structure!
  
*You have a graphic called H-Chart Mod 7.png in your files. This is the hierarchy chart for this program. It clearly shows where each function should be called from.*


Your program must effectively handle ALL errors. I should see no "red" program errors while running and testing your code.
The program should not end or quit until the user chooses to quit in the menu.

You should notice that this program's calculations are similar to a program we covered in class subject reviews and in another project. However, the flow of the program is very different!
To pass the tests, you need to have your output look like mine, but work with any numbers and selection entered:
```    
Select the action you'd like to take, by number:
  1. Add
  2. Subtract
  3. Multiply
  4. Divide
  5. Modulo
  6. Exponent
  Any other number to exit the program
Enter the menu item you would like to run: 4
Enter your first number: 5
Enter your second number: 3
5.0 / 3.0 = 1.6666666666666667

Select the action you'd like to take, by number:
  1. Add
  2. Subtract
  3. Multiply
  4. Divide
  5. Modulo
  6. Exponent
  Any other number to exit the program
Enter the menu item you would like to run: 4
Enter your first number: 5
Enter your second number: 0
5.0 / 0.0 = Divide by 0 Not Allowed

Select the action you'd like to take, by number:
  1. Add
  2. Subtract
  3. Multiply
  4. Divide
  5. Modulo
  6. Exponent
  Any other number to exit the program
Enter the menu item you would like to run: 5
Enter your first number: 5
Enter your second number: 0
5.0 % 0.0 = Divide by 0 Not Allowed

Select the action you'd like to take, by number:
  1. Add
  2. Subtract
  3. Multiply
  4. Divide
  5. Modulo
  6. Exponent
  Any other number to exit the program
Enter the menu item you would like to run: 7
Program Exiting

```

A hint for using userInput() and inputTest()

* main() calls userInput()

**userInput()** 
* Asks user for menu number. 
* Passes that number to inputTest() to determine if it's a compatible number type (IE: not a string). Continues to ask for a valid number until a valid number is input. Returns valid number to userInput().
* Determines if the compatible number is in the range of menu items. If so, then it continues.  If not, then return the out of range number and two other values to main() so the program can continue / end.
* Asks user for first calculator number.
* Passes that number to inputTest() to determine if it's a compatible number type. Returns it to userInput() if it is compatible.
* Asks user for second calculator number
* Passes that number to inputTest() to determine if it's a compatible number type. Returns it to userInput() if it is compatible.
* Returns all three numbers to main()

**inputTest()**
* Accepts one value
* Determine if the value is a compatible type (hint: try/except will throw an error if you attempt to cast a string to an int or float).
* Return a compatible type to userInput

