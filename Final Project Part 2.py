# Put your name here:

# Don't change this line:
from datetime import datetime

# Put your program here
def main():
  banner()
  modifiedCDCFile = openCDCfile()
  while True:
    menuValue = menu()
    if menuValue == 1:
      menu()
    elif menuValue == 2:
      defaultReport(modifiedCDCFile)
    elif menuValue == 3:
      totalMortalityByState()
    elif menuValue == 4:
      reportSingleStateByDate()
    elif menuValue == 5:
      getHighestMortality()
    elif menuValue == 6:
      print('Exiting program')
      break


def banner():
  print("""                                                                                                   
                                                                 ''''''                            
DDDDDDDDDDDDD             OOOOOOOOO     NNNNNNNN        NNNNNNNN '::::'TTTTTTTTTTTTTTTTTTTTTTT     
D::::::::::::DDD        OO:::::::::OO   N:::::::N       N::::::N '::::'T:::::::::::::::::::::T     
D:::::::::::::::DD    OO:::::::::::::OO N::::::::N      N::::::N ':::''T:::::::::::::::::::::T     
DDD:::::DDDDD:::::D  O:::::::OOO:::::::ON:::::::::N     N::::::N':::'  T:::::TT:::::::TT:::::T     
  D:::::D    D:::::D O::::::O   O::::::ON::::::::::N    N::::::N''''   TTTTTT  T:::::T  TTTTTT     
  D:::::D     D:::::DO:::::O     O:::::ON:::::::::::N   N::::::N               T:::::T             
  D:::::D     D:::::DO:::::O     O:::::ON:::::::N::::N  N::::::N               T:::::T             
  D:::::D     D:::::DO:::::O     O:::::ON::::::N N::::N N::::::N               T:::::T             
  D:::::D     D:::::DO:::::O     O:::::ON::::::N  N::::N:::::::N               T:::::T             
  D:::::D     D:::::DO:::::O     O:::::ON::::::N   N:::::::::::N               T:::::T             
  D:::::D     D:::::DO:::::O     O:::::ON::::::N    N::::::::::N               T:::::T             
  D:::::D    D:::::D O::::::O   O::::::ON::::::N     N:::::::::N               T:::::T             
DDD:::::DDDDD:::::D  O:::::::OOO:::::::ON::::::N      N::::::::N             TT:::::::TT           
D:::::::::::::::DD    OO:::::::::::::OO N::::::N       N:::::::N             T:::::::::T           
D::::::::::::DDD        OO:::::::::OO   N::::::N        N::::::N             T:::::::::T           
DDDDDDDDDDDDD             OOOOOOOOO     NNNNNNNN         NNNNNNN             TTTTTTTTTTT           
PPPPPPPPPPPPPPPPP        AAA               NNNNNNNN        NNNNNNNNIIIIIIIIII      CCCCCCCCCCCCC   
P::::::::::::::::P      A:::A              N:::::::N       N::::::NI::::::::I   CCC::::::::::::C   
P::::::PPPPPP:::::P    A:::::A             N::::::::N      N::::::NI::::::::I CC:::::::::::::::C   
PP:::::P     P:::::P  A:::::::A            N:::::::::N     N::::::NII::::::IIC:::::CCCCCCCC::::C   
  P::::P     P:::::P A:::::::::A           N::::::::::N    N::::::N  I::::I C:::::C       CCCCCC   
  P::::P     P:::::PA:::::A:::::A          N:::::::::::N   N::::::N  I::::IC:::::C                 
  P::::PPPPPP:::::PA:::::A A:::::A         N:::::::N::::N  N::::::N  I::::IC:::::C                 
  P:::::::::::::PPA:::::A   A:::::A        N::::::N N::::N N::::::N  I::::IC:::::C                 
  P::::PPPPPPPPP A:::::A     A:::::A       N::::::N  N::::N:::::::N  I::::IC:::::C                 
  P::::P        A:::::AAAAAAAAA:::::A      N::::::N   N:::::::::::N  I::::IC:::::C                 
  P::::P       A:::::::::::::::::::::A     N::::::N    N::::::::::N  I::::IC:::::C                 
  P::::P      A:::::AAAAAAAAAAAAA:::::A    N::::::N     N:::::::::N  I::::I C:::::C       CCCCCC   
PP::::::PP   A:::::A             A:::::A   N::::::N      N::::::::NII::::::IIC:::::CCCCCCCC::::C   
P::::::::P  A:::::A               A:::::A  N::::::N       N:::::::NI::::::::I CC:::::::::::::::C   
P::::::::P A:::::A                 A:::::A N::::::N        N::::::NI::::::::I   CCC::::::::::::C   
PPPPPPPPPPAAAAAAA                   AAAAAAANNNNNNNN         NNNNNNNIIIIIIIIII      CCCCCCCCCCCCC   
                                                                                                                  
                                                                                                   """)


def menu():
  print('\nMortality Rate Comparison Menu\n\n1.  Show This Menu Again\n2.  Full Mortality Report by State\n3.  Mortality for a Single State, by Date Range\n4.  Mortality Summary for all States\n5. Highest COVID mortality Week\n6.  Exit\n'
    )
  userMenuSelection = input('Make your selection from the menu: ')
  while True:
    try:
      userMenuSelection = int(userMenuSelection)
    except:
      print(userMenuSelection, 'is not a valid number')
      userMenuSelection = input('Please enter a valid number: ')
    else:
      if userMenuSelection in range(1, 7):
        return userMenuSelection
      else:
        print("Please enter a valid menu selection: ")

def getUserInputDates():
  getAvailableDates()

def getAvailableDates():
  openCDCfile()
  minDate = 

def reportSingleStateByDate():
  userState = input('Please enter your selected state: ')
  getUserInputDates()
  reportStateDate = open('Mortality_For_State_By_Date_Range_Report.txt')

def totalMortalityByState():
  reportMortalityState = open('Mortality_Summary_For_All_States_By_Date_Range_Report.txt')
  

def printLineDetailReport(fileHandler,State,totalDeathSum,totalNaturalCause,totalC19MC,totalC19UC):
  #totalDeathSum = str(totalDeathSum)
  #totalNaturalCause = str(totalNaturalCause)
  #totalC19MC = str(totalC19MC)
  #totalC19UC = str(totalC19UC)

def getHighestMortality():
  #highestMortality = max(mortality)
  #maxWeek = dates[mortality.index(highestMortality)]
  #maxState = state[mortality.index(highestMortality)]
  #maxNaturalCause = nC[mortality.index(highestMortality)]
  #covidPercentage = highestMortality / maxNaturalCause * 100
  #print('This represents ', covidPercentage, '% of the toatl reported deaths in ', maxState, ' that week.', sep='')

def openCDCfile():
  dataFromFile = open('cdc.csv', 'r')
  dataLines = dataFromFile.readlines()
  modifiedCDCFile = open('cdc.csv', 'w')
  for number, line in enumerate(dataLines):
    if number not in range(0,7):
      modifiedCDCFile.write(line)
  modifiedCDCFile.close() 
  return modifiedCDCFile


def defaultReport(modifiedCDCFile):
  modifiedCDCFile = open('cdc.csv','r')
  dataLines = modifiedCDCFile.readlines()
  newFile = open('Full_Mortality_By_State_Report.txt','w')
  reportName = 'National Mortality Rate by Cause Listed by State and Reporting Date Report  Sorted by State'
  newFile.write(reportName)
  now = datetime.now()
  dt_string = now.strftime("%m/%d/%Y     %H:%M:%S")
  newFile.write('\nReport Generated: '+dt_string+'\n')
  header = 'STATE\t\t\tWEEK ENDING\t\t\tTOTAL DEATHS\t\t\tNATURAL CAUSES\t\t\tC19 MULTIPLE CAUSES\t\t\tC19 UNDERLYING CAUSE'
  newFile.write(header)
  for line in dataLines: 
    line = line.rstrip()
    s,_,_,w,tD,nC,_,_,_,_,_,_,_,_,_,_,_,mC,uC = line.split(',')
    w = w.rjust(11,' ')
    tD = tD.rjust(17,' ')
    nC = nC.rjust(18,' ')
    mC = mC.rjust(21,' ')
    uC = uC.rjust(25,' ')
    line = (f'{s}{w}{tD}{nC}{mC}{uC}')
    newFile.write(f'\n{line}\n')
  print('\nFull Report Posted')  


# ----------------------------------------------------------------------
# Put all of your code ABOVE this block of code
# This next code block MUST be at the very bottom of your program.
# Leave everthing below this line alone!
# Make no changes below this line!
# --------------------------------

###  HELPER FUNCTION FOR YOU ###


# use this function when you need to compare date strings
# you can't actually compare strings that "look" like dates
# because they aren't date objects. They won't sort like you
# expect them to.
# This function accepts date in mm/dd/yyyy format as a string
# returns date in yy/mm/dd format as a date object (not a string!!!)
def convertDate(dateString):
	objDate = datetime.strptime(dateString, '%m/%d/%Y')
	return objDate


# Recall that you can't perform math functions on empty strings.
# Use this function to replace blank values with zero so that any math will work
def replaceSpaceWithZero(uString):
	if uString == '':
		uString = 0
	return int(uString)


# I've called main() for you.
# This line is a special way to call main
# that allows me to test your code.  Do not change it!
if __name__ == '__main__':
	main()
