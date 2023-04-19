# comments start with the hash.  
# Be sure to read these!
# Put your name here: Nadia Schuld

# Type the code below here:

def main():
  openedWeatherFile = readFile()
  reportAll(openedWeatherFile)
  findHighTemp(openedWeatherFile)

def readFile():
  openedWeatherFile = open('ROAWeather.csv')
  openedWeatherFile = openedWeatherFile.replace
  return openedWeatherFile
  

def reportAll(openedWeatherFile):
  openedWeatherFile = open('ROAWeather.csv')
  for line in openedWeatherFile:
    line = line.rstrip()
    line.replace('\""','').replace(',','  ')
    line.write()
  openedWeatherFile.close()
  
def findHighTemp():
  pass
  

def printHighValues():
  pass

  
  

# Make no changes below this line!
# --------------------------------
# I've called main() for you.
# This line is a special way to call main
# that allows me to test your code.  Do not change it!
if __name__ == '__main__':
    main()