# Your Name: Nadia Schuld

#creates a function called main()
#this function controls the flow of the program
def main():
  #calls the userInput() function and accepts the userSentence variable
  #assigns the userSentence variable to the userString variable 
  userString = userInput()
  #calls the printTriangleUp(userString) function
  #passes the userString variable to the function
  printTriangleUp(userString)
  #calls the printTriangleUp(userString) function and accepts the counter variable
  #assigns the counter variable to the counter variable in the main() function 
  counter = printTriangleUp(userString)
  #calls the printTriangleDown(userString, counter) function 
  #passes the userString and counter variables to the function
  printTriangleDown(userString, counter)
  #calls the printTriangleDown(userString, counter) function and accepts the counter variable
  #assigns the counter variable to the finalCounter variable
  finalCounter = printTriangleDown(userString, counter)
  #calls the countUser(finalCounter) function
  #passes the finalCounter variable to the function
  countUser(finalCounter)

#creates a function called userInput()
#asks the user to enter a sentence
def userInput():
  #creates a variable called userSentence and accepts user input as a string
  userSentence = input('Enter a short sentence: ')
  #returns the userSentence variable to the calling function
  return userSentence

#creates a function called printTriangleUp(userString)
#accepts the userString variable from main() 
def printTriangleUp(userString):
  #creates a counter variable and assigns it a value of 0 
  counter = 0
  #creates a variable called stringLength and sets it equal to the length of the userString variable
  stringLength = len(userString)
  #creates a for loop that loops the index variable for a value of 0 to the value of the stringLength variable
  for index in range(stringLength):
    #creates a for loop that loops the stringLetter variable for a value of 0 to the value of the index variable + 1 
    for stringLetter in range(index+1):
      #creates a user friendly print statement that prints the userString variable with an index equal to the stringLetter variable
      #displays user friendly print statement on user display
      #end='' prevents the line from ending
      print(userString[stringLetter], end='')
      #adds 1 to the counter for each iteration of the loop
      counter += 1
    #print statement starts on a new line 
    print()
  #returns counter variable to the calling function
  return counter

#creates a function called printTriangleDown(userString, counter)
#accepts the userString and counter variables from main()
def printTriangleDown(userString, counter):
  #sets the counter variable equal to the value that was received from main()
  counter = counter
   #creates a variable called stringLength and sets it equal to the length of the userString variable
  stringLength = len(userString)
   #creates a for loop that loops the index variable from the value of the stringLength variable to a value of 0
  #for loop counts down by one during each iteration
  for index in range(stringLength, 0, -1):
    #creates a for loop that loops the stringLetter variable from the value of  0 to the value of the index variable - 1 
    for stringLetter in range(index-1):
      #creates a user friendly print statement that prints the userString variable with an index equal to the stringLetter variable
      #displays user friendly print statement on user display
      #end='' prevents the line from ending
      print(userString[stringLetter], end='')
       #adds 1 to the counter for each iteration of the loop
      counter += 1
    #print statement starts on a new line 
    print()
  #returns counter variable to the calling function
  return counter

#creates a function called countUser(finalCounter)
#accepts the finalCounter variable from main() 
def countUser(finalCounter):
 #creates a user friendly print statement that prints a string using the variable finalCounter
  #displays the user friendly print statement on the user display
  print('Total Count: ', finalCounter)

#calls the main() function 
main()





#P.S. I'm aware that the output isn't correct I didn't know how to get rid of the extra blocks of text 