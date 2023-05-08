# Put your name here:

# Don't change this line:
from datetime import datetime

# Put your program here

#controls the flow of the program
#calls other functions
#loops through menu to determine what reports are generated
#accepts one file handler
#accepts one integer
#passes one file handler 
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
      reportSingleStateByDate()
    elif menuValue == 4:
      totalMortalityByState()
    elif menuValue == 5:
      getHighestMortality()
    elif menuValue == 6:
      print('\nExiting program')
      break

#creates a banner for the UI using ASCII 
#prints banner on user display
#accepts nothing 
#passes nothing
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

#creates a user friendly menu for different comparisons
#validates user input and asks for valid input if none is entered 
#uses a while True loop and decision logic to validate user input
#accepts nothing 
#passes nothing
def menu():
  print('\nMortality Rate Comparison Menu\n\n1.  Show This Menu Again\n2.  Full Mortality Report by State\n3.  Mortality for a Single State, by Date Range\n4.  Mortality Summary for all States\n5.  Highest COVID mortality Week\n6.  Exit\n'
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

#opens the CDC.csv file 
#writes file to remove unnecessary lines from the file
#uses a for loop and decision logic to iterate through each line 
#accepts nothing 
#passes one file handler 
def openCDCfile():
  dataFromFile = open('cdc.csv', 'r')
  dataLines = dataFromFile.readlines()
  modifiedCDCFile = open('cdc.csv', 'w')
  for number, line in enumerate(dataLines):
    if number not in range(0,7):
      modifiedCDCFile.write(line)
  modifiedCDCFile.close() 
  return modifiedCDCFile

#generates the full mortality report 
#uses CDC file to generate new report 
#adds a header to the report 
#adds the current date and time to the report 
#separates the state, end week date, total deaths, deaths by natural causes, COVID 19 deaths with multiple causes, and COVID 19 deaths with underlying causes from the CDC file 
#accepts one file handler
#passes nothing
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
  print('\nFull Report Posted under file name "Full_Mortality_By_State_Report.txt"')  

#function not completed currently does nothing 
#accepts nothing 
#passes nothing 
def getUserInputDates():
  pass
  #getAvailableDates()

#function not completed currently does nothing 
#accepts nothing 
#passes nothing 
def getAvailableDates():
 pass
  #openCDCfile()
  #minDate = 

#function not completed currently does nothing 
#accepts nothing 
#passes nothing 
def reportSingleStateByDate():
  pass
  #userState = input('Please enter your selected state: ')
  #getUserInputDates()
  #reportStateDate = open('Mortality_For_State_By_Date_Range_Report.txt')

#generates a report that summarizes total mortality by state
#writes a header to the new report
#writes the current date and time to the new report 
#creates lists to separate the state, total deaths, number of deaths by natural causes, COVID 19 deaths with multiple causes, and COVID 19 deaths with underlying causes 
#iterates through each state in the state list to calculate the total deaths, sum of natural deahts, sum of COVID 19 deaths with multiple and underlying causes based on staticmethod
#accepts nothing 
#calls printLineDetailReport 
#passes one file handler 
#passes one string 
#passes 4 integers 
def totalMortalityByState():
  dataFromFile = open('cdc.csv','r')
  dataLines = dataFromFile.readlines()
  reportMortalityState = open('Mortality_Summary_For_All_States_By_Date_Range_Report.txt','w')
  reportName = 'Mortality Summary For All States By Entire Date Range Report'
  reportMortalityState.write(reportName)
  now = datetime.now()
  dt_string = now.strftime("%m/%d/%Y     %H:%M:%S")
  reportMortalityState.write('\nReport Generated: '+dt_string+'\n')
  header = 'STATE\t\t\tTOTAL DEATHS\t\t\tNATURAL CAUSES\t\t\tC19 MULTIPLE CAUSES\t\t\tC19 UNDERLYING CAUSE'
  reportMortalityState.write(header)
  state = []
  totalDeaths = []
  naturalCauses = []
  c19MC = []
  c19UC = [] 
  for line in dataLines:
    line = line.rstrip()
    s,_,_,_,tD,nC,_,_,_,_,_,_,_,_,_,_,_,mC,uC = line.split(',')
    state.append(s)
    tD = replaceSpaceWithZero(tD)
    totalDeaths.append(int(tD))
    nC = replaceSpaceWithZero(nC)
    naturalCauses.append(int(nC))
    mC = replaceSpaceWithZero(mC)
    c19MC.append(int(mC))
    uC = replaceSpaceWithZero(uC)
    c19UC.append(int(uC))
  for each in state: 
    sumTotalDeaths = sum(totalDeaths)
    sumNaturalCauses = sum(naturalCauses)
    sumC19MC = sum(c19MC)
    sumC19UC = sum(c19UC)
  printLineDetailReport(reportMortalityState,state,sumTotalDeaths,sumNaturalCauses,sumC19MC,sumC19UC)

#writes the data to the generated report from the totalMortalityByState() function
#converts the accepted integers into strings 
#creates a user friendly print statement to let the user know the report was generated 
#accepts one file handler 
#accepts one string
#accepts four integers
#passes nothing 
def printLineDetailReport(reportMortalityState,state,totalDeathSum,totalNaturalCause,totalC19MC,totalC19UC):
  reportMortalityState = open('Mortality_Summary_For_All_States_By_Date_Range_Report.txt','a')
  totalDeathSum = str(totalDeathSum)
  totalNaturalCause = str(totalNaturalCause)
  totalC19MC = str(totalC19MC)
  totalC19UC = str(totalC19UC)
  line = (f'{state}{totalDeathSum}{totalC19MC}{totalC19UC}')
  reportMortalityState.write(f'\n{line}\n')
  print('\nFull Report Posted under file name "Mortality_Summary_For_All_States_By_Date_Range_Report.txt"')

#creates a user friendly statement that displays the highest mortality from the CDC file 
#creates lists to separate the state, end week date, number of deaths by natural causes, and COVID 19 deaths with underlying causes 
#finds the week and corresponding state that had the highest amount of COVID 19 deaths with underlying causes
#calculates the percentage of deahts from natural causes that were COVID 19 deaths with underlying causes 
#accepts nothing 
#passes nothing 
def getHighestMortality():
  dataFromFile = open('cdc.csv','r')
  dataLines = dataFromFile.readlines()
  state = []
  dates = []
  naturalCause = []
  mortality = []
  for line in dataLines:
    line = line.rstrip()
    s,_,_,w,_,nC,_,_,_,_,_,_,_,_,_,_,_,_,uC = line.split(',')
    state.append(s)
    dates.append(w)
    naturalCause.append(int(nC))
    uC = replaceSpaceWithZero(uC)
    mortality.append(int(uC))
  highestMortality = max(mortality)
  maxWeek = dates[mortality.index(highestMortality)]
  maxState = state[mortality.index(highestMortality)]
  maxNaturalCause = naturalCause[mortality.index(highestMortality)]
  covidPercentage = highestMortality / maxNaturalCause * 100
  print('\n\nThe largest number of deaths directly attributible to COVID 19 in this report range was ', highestMortality, ' in ', maxState, ' during the week of ', maxWeek, '.', sep = '')
  print('\nThis represents ', format(covidPercentage,'.2f'), '% of the total reported deaths in ', maxState, ' that week.', sep='')

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
