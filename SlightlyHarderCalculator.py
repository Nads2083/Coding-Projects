# Your Name: Nadia Schuld

#creates a function called manin()
#this function controls the flow of the program
def main():
  #creates a while loop that continues until break
  while True:
    #calls userMenu() function
    userMenu()
    #calls userInput() function
    #accepts a validated menu choice from user
    #accepts validated user numbers from user 
    #accepts a validated menu choice and two Falses if user enters a number other than 1-6 for menu choice
    #assigns validated menu choice and validated user numbers to variables userMenuChoice, userNumber1, and userNumber2
    userMenuChoice, userNumber1, userNumber2 = userInput()
    #checks to see if the userMenuChoice variable is equal to 1
    if userMenuChoice == 1:
      #assigns the string '+' to variable named operatorSign
      operatorSign = '+'
      #assigns numberSum variable from add(userNumber1, userNumber2) function to calculatedAnswer variable
      calculatedAnswer = add(userNumber1, userNumber2)
    #checks to see if the userMenuChoice variable is equal to 2
    elif userMenuChoice == 2:
      #assigns the string '-' to variable named operatorSign
      operatorSign = '-'
       #assigns numberSubtract variable from subtract(userNumber1, userNumber2) function to calculatedAnswer variable
      calculatedAnswer = subtract(userNumber1, userNumber2)
    #checks to see if the userMenuChoice variable is equal to 3
    elif userMenuChoice == 3:
      #assigns the string '*' to variable named operatorSign
      operatorSign = '*'
      #assigns numberMultiply variable from multiply(userNumber1, userNumber2) function to calculatedAnswer variable
      calculatedAnswer = multiply(userNumber1, userNumber2)
    #checks to see if the userMenuChoice variable is equal to 4
    elif userMenuChoice == 4:
      #assigns the string '/' to variable named operatorSign
      operatorSign = '/'
      #assigns numberDivide variable from divide(userNumber1, userNumber2) function to calculatedAnswer variable
      calculatedAnswer = divide(userNumber1, userNumber2)
    #checks to see if the userMenuChoice variable is equal to 5
    elif userMenuChoice == 5:
      #assigns the string '%' to variable named operatorSign
      operatorSign = '%'
      #assigns numberModulo variable from modulo(userNumber1, userNumber2) function to calculatedAnswer variable
      calculatedAnswer = modulo(userNumber1, userNumber2)
   #checks to see if the userMenuChoice variable is equal to 6
    elif userMenuChoice == 6:
      #assigns the string '**' to variable named operatorSign
      operatorSign = '**'
      #assigns numberExponent variable from exponent(userNumber1, userNumber2) function to calculatedAnswer variable
      calculatedAnswer = exponent(userNumber1, userNumber2)
    #runs if userMenuChoice is not in the range of 1 to 7 
    else: 
      #creates user friendly print statement
      #displays print statement on user display
      print('Program Exiting')
     #exits while True loop and runs the rest of the program
      break
    #calls userOutput and passes userNumber1, userNumber2, operatorSign, and calculatedAnswer variables
    userOutput(userNumber1, userNumber2, operatorSign, calculatedAnswer)
    
#creates a function called userMenu()
#creates print statement of menu options 
def userMenu():
  #creates user friendly print statement of different menu options 
  #displays print statement on user display
  print("\nSelect the action you'd like to take, by number:\n  1. Add\n  2. Subtract\n  3. Multiply\n  4. Divide\n  5. Modulo\n  6. Exponent\n  Any other number to exit the program")

#creates a function called userInput()
#accepts user input and assigns it to variables
#passes created variable to inputTest() function to test for valid numbers
def userInput():
  #creates a variable called userNumber and accepts user input for menu choice as a string
  userNumber = input('Enter the menu item you would like to run: ')
  #sends userNumber to the inputTest function and assigns it to the validMenuChoice variable 
  validMenuChoice = inputTest(userNumber)
  #checks to see if the validMenuChoice variable is in the range of 1 to 7
  if validMenuChoice in range(1,7):
    #accepts user input for first calculator number as a string and reassigns the userNumber variable
    userNumber = input('Enter your first number: ')
    #sends userNumber to the inputTest function and assigns it to the validFirstNumber variable 
    validFirstNumber = inputTest(userNumber)
    #accepts user input for second calculator number as a string and reassigns the userNumber variable
    userNumber = input('Enter your second number: ')
     #sends userNumber to the inputTest function and assigns it to the validSecondNumber variable
    validSecondNumber = inputTest(userNumber)
    #returns the validMenuChoice, validFirstNumber, and validSecondNumber variables to the main() function
    return validMenuChoice, validFirstNumber, validSecondNumber
  #runs if validMenuChoice is not in the range of 1 to 7
  else:
    #returns validMenuChoice and two False values to the main() function
    return validMenuChoice, False, False

#creates a function called inputTest()
#accepts the userNumber variable from the userInput() function
#tests if userNumber is a valid number and returns it to userInput()
def inputTest(userInputVariable):
  #creates a while True loop that continues until break 
  while True:
    #uses try to test code for errors 
    try:
      #casts the userInputVariable as a float
      userInputVariable = float(userInputVariable)
   #exception to run if code bloak throws an error 
    except:
      #creates a print statement that tells the user the number they entered is not a valid number
      #displays the user friendly print statement on the user display
      print(userInputVariable,'is not a valid number')
      #creates an input statement that asks the user to enter a valid number
      #assigns user input to userInputVariable variable 
      userInputVariable = input('Please enter a valid number: ')
    #runs if there are no errors in the code 
    else:
      #returns the userInputVariable to the main() function and breaks the while True loop
      return userInputVariable
          
#creates a function called add(a1,a2)
#receives userNumber1 and userNumber2 variables from the main() function
def add(a1, a2):
  #calculates the sum of variables entered by the user
  #assigns calculated sum to the variable numberSum
  numberSum = a1 + a2 
  #returns the numberSum variable to the calling function
  return numberSum
  
#creates a function called subtract(s1,s2)
#receives userNumber1 and userNumber2 variables from the main() function
def subtract(s1, s2):
  #calculates the difference of variables entered by the user
  #assigns calculated difference to the variable numberSubtract
  numberSubtract = s1 - s2
  #returns the numberSubtract variable to the calling function
  return numberSubtract
  
#creates a function called multiply(m1,m2)
#receives userNumber1 and userNumber2 variables from the main() function
def multiply(m1, m2):
  #calculates the product of variables entered by the user
  #assigns calculated product to the variable numberMultiply
  numberMultiply = m1 * m2
  #returns the numberMultiply variable to the calling function
  return numberMultiply

#creates a function called divide(d1,d2)
#receives userNumber1 and userNumber2 variables from the main() function
def divide(d1,d2):
  #use try to watch code for errors
  try:
  #calculates the quotient of variables entered by the user
  #assigns calculated quotient to the variable numberDivide
    numberDivide = d1 / d2
    #returns the numberDivide variable to the main() function
    return numberDivide
  #exception to run if code block throws an error 
  except:
  #returns a user friendly string to the calling function
    return 'Divide by 0 Not Allowed'

#creates a function called modulo(moo1,moo2)
#receives userNumber1 and userNumber2 variables from the main() function
def modulo(moo1,moo2):
  #use try to watch code for errors
  try:
    #calculates the remainder of variables entered by the user
  #assigns calculated remainder to the variable numberModulo
    numberModulo = moo1 % moo2
    #returns the numberModulo variable to the main() function
    return numberModulo
  #exception to run if code block throws an error
  except:
  #returns a user friendly string to the calling function
    return 'Divide by 0 Not Allowed'
  
#creates a function called exponent(e1,e2)
#receives userNumber1 and userNumber2 variables from the main() function
def exponent(e1,e2):
  #calculates the first variable raised to the power of the second variable entered by the user
  #assigns calculated value to the variable numberExponent
  numberExponent = e1 ** e2
   #returns the numberExponent variable to the calling function
  return numberExponent

#creates a function called userOutput(userNumber1, userNumber2, operatorSign, CalculatedAnswer)
#accepts userNumber1, userNumber2, operatorSign, and calculatedAnswer variables from the main() function
def userOutput(userNumber1, userNumber2, operatorSign, calculatedAnswer):
  #creates a print statement using the userNumber1, userNumber2, operatorSign, and calculatedAnswer variables
  #displays the user friendly print statement on the user display 
  print(userNumber1, operatorSign, userNumber2, '=', calculatedAnswer)


# Put all of your code ABOVE this block of code
# This next code block MUST be at the very bottom of your program.
# Leave everthing below this line alone!
# --------------------------------
# I've called main() for you.
# This line is a special way to call main
# that allows me to test your code.  Do not change it!
if __name__ == '__main__':
    main()