# Your Name: Nadia Schuld

def main():
  while True:
    numberList = []
    print(type(numberList))
    userNumber = float(input('Enter an integer, or "0" to Stop:'))
    if userNumber > 0:
      print('in if statement')
      numberList = numberList.append(userNumber)
      print(type(numberList))
    else:
      average = sum(numberList) / len(numberList)
      average = float(average)
      print('The average of your numbers is',average)
      break
main()