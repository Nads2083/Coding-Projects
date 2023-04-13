# Put your name here: Nadia Schuld

def main():
  openHeadersFile = open('headers.txt')
  counter = showRecords(openHeadersFile)
  userPrint(counter)

def showRecords(openHeaders):
  counter = 0
  for line in openHeaders:
    if line.startswith('Return-Path:'):
      line = line.rstrip()
      counter += 1
      print(line)
  return counter

def userPrint(counter):
   print('Found',counter,'records.')

main()


