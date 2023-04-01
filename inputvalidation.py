def inputvalidation(inputVar):
    while type(inputVar) != int:
        try:
            inputVar = float(inputVar)
        except:
            print('That is not a valid number')
            inputVar = input('Please supply a valid number')
        else:
            return(inputVar)

userinput = input('what is the number :')
validVar = inputvalidation(userinput)
print(validVar)