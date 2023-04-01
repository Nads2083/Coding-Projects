

def main(): #Controls the flow of the program (calls the other modules). This includes decision logic (such as while True, if/elif/else) to call functions as requested. 
    while True:
        userMenu()
        (action,value1,value2)=userInput()
        if action not in range(1,7):
            print ('thank you come again')
            break
        else:
            print(f'do maths with vars action#:{action}, var1#:{value1}, var2#:{value2}') 



def userMenu(): #Displays choices.
    pass






def userInput(): #Asks the user to select a menu option. If any menu item is selected, ask to enter two numbers. Hint: Don't cast the input to number types. Let inputTest() do that.
    rawUserInput = input('Enter the menu Item you would like to run')
    validMenuChoice = inputTest(rawUserInput)
    print(f'your menu choice is {validMenuChoice}')
    
    if validMenuChoice in range(1,7):
        
        rawUserInput = input('Please enter your first number')
        validCompNumber1 = inputTest(rawUserInput)
        print(f'Your first number is {validCompNumber1}')

        rawUserInput = input('Please enter your second number')
        validCompNumber2 = inputTest(rawUserInput)
        print(f'Your second number is {validCompNumber2}')
        
        return(validMenuChoice,validCompNumber1,validCompNumber2)
    
    else:
        return(validMenuChoice,False,False)
    



def inputTest(inputVar): #Accepts one value from userInput(). Tests value to make sure it's a number. If it's not a number, it will ask for a valid number. This is one of the few times you can have a user input values in a function other than "userInput(). Returns valid numbers.
    while type(inputVar) != int:
            try:
                inputVar = float(inputVar)
            except:
                print(f'{inputVar} is not a valid number')
                inputVar = input('Please supply a valid number')
            else:
                return(inputVar)



def add(validCompNumber1,validCompNumber2): #Accepts two numbers, returns the sum
    pass




def subtract(validCompNumber1,validCompNumber2): #Accepts two numbers, returns the difference of the first number minus the second number
    pass




def multiply(validCompNumber1,validCompNumber2): #Accepts two numbers, returns the product
    pass




def divide(validCompNumber1,validCompNumber2): #Accepts two numbers, returns the quotient of the first number divided by the second number
    pass




def modulo(validCompNumber1,validCompNumber2): #Accepts two numbers, returns the modulo of the first number divided by the second number
    pass






def exponent(validCompNumber1,validCompNumber2): #Accepts two numbers, returns the first number raised to the power of the second number.
    pass






def userOutput(validCompNumber1,validCompNumber2): #Gives a user friendly output of the selected calculation. HINT: make your code reusable so that this method contains no decision structure!
    pass


main()