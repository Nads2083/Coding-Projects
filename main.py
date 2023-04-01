# Your Name: Nadia Schuld

def main():
  while True:
    userMenu()
    userInput()
    if userinput() == 1:
      add(number1, number2)
    elif userinput() == 2:
      subtract(number1, number2)
    elif userinput() == 3:
      multiply(number1, number2)
    elif userinput() == 4:
      divide(number1, number2)
    elif userinput() == 5:
      modulo(number1, number2)
    elif userInput() == 6:
      exponent(number1, number2)
    else: 
      print('Progam Exiting')

  
  userOutput()
  
def userMenu():
  print("\nSelect the action you'd like to take, by number:")
  print('  1. Add' '\n  2. Subtract' '\n  3. Multiply' '\n  4. Divide' '\n  5. Modulo' '\n  6. Exponent')
  print('  Any other number to exit the program')

def userInput():
  menuChoice = input('Enter the menu item you would like to run: ')
  return menuChoice
  if menuChoice in range(1,7):
    print('in if statement')
    firstNumber = input('Enter your first number: ')
    return firstNumber
    secondNumber = input('Enter your second number: ')
    return secondNumber
    return menuChoice, firstNumber, secondNumber
  else:
    return menuChoice

def userTest(menuChoice, firstNumber, secondNumber):
  
  
  
#creates a function called add(a1,a2)
#receives number1 and number2 variables from the main() function
def add(a1, a2):
  #calculates the sum of variables entered by the user
  #assigns calculated sum to the variable numberSum
  numberSum = a1 + a2 
  #returns the answer variable to the calling function
  return numberSum
  
#creates a function called subtract(s1,s2)
#receives number1 and number2 variables from the main() function
def subtract(s1, s2):
  #calculates the difference of variables entered by the user
  #assigns calculated difference to the variable numberSubtract
  numberSubtract = s1 - s2
  #returns the answer variable to the calling function
  return numberSubtract
  
#creates a function called multiply(m1,m2)
#receives number1 and number2 variables from the main() function
def multiply(m1, m2):
  #calculates the product of variables entered by the user
  #assigns calculated product to the variable numberMultiply
  numberMultiply = m1 * m2
  #returns the answer variable to the calling function
  return numberMultiply

#creates a function called divide(d1,d2)
#receives number1 and number2 variables from the main() function
def divide(d1,d2):
  #use try to watch code for errors
  try:
  #calculates the quotient of variables entered by the user
  #assigns calculated quotient to the variable numberDivide
    numberDivide = d1 / d2
    return numberDivide
  #exception to run if code block throws an error 
  except:
  #returns a user friendly string to the calling function
    return 'Divide by 0 Not allowed'

#creates a function called modulo(moo1,moo2)
#receives number1 and number2 variables from the main() function
def modulo(moo1,moo2):
  #use try to watch code for errors
  try:
    #calculates the remainder of variables entered by the user
  #assigns calculated remainder to the variable numberModulo
    numberModulo = moo1 % moo2
    return numberModulo
  #exception to run if code block throws an error
  except:
  #returns a user friendly string to the calling function
    return 'Divide by 0 Not Allowed'
  
#creates a function called exponent(e1,e2)
#receives number1 and number2 variables from the main() function
def exponent(e1,e2):
  #calculates the first variable raised to the power of the second variable entered by the user
  #assigns calculated value to the variable numberExponent
  numberExponent = e1 ** e2
   #returns the answer variable to the calling function
  return numberExponent

def userOutput():



# Put all of your code ABOVE this block of code
# This next code block MUST be at the very bottom of your program.
# Leave everthing below this line alone!
# --------------------------------
# I've called main() for you.
# This line is a special way to call main
# that allows me to test your code.  Do not change it!
if __name__ == '__main__':
    main()