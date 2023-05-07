# Put your name here: Nadia Schuld

# comments start with the hash.
# Be sure to read these!

# Don't change this line:
from datetime import datetime


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
      print('Function not implemented yet')
    elif menuValue == 4:
      print('Function not implemented yet')
    elif menuValue == 5:
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
  print('\nMortality Rate Comparison Menu\n\n1.  Show This Menu Again\n2.  Full Mortality Report by State\n3.  Mortality for a Single State, by Date Range\n4.  Mortality Summary for all States\n5.  Exit\n'
    )
  userMenuSelection = input('Make your selection from the menu: ')
  while True:
    try:
      userMenuSelection = int(userMenuSelection)
    except:
      print(userMenuSelection, 'is not a valid number')
      userMenuSelection = input('Please enter a valid number: ')
    else:
      if userMenuSelection in range(1, 6):
        return userMenuSelection
      else:
        print("Please enter a valid menu selection: ")


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
  

# Put all of your code ABOVE this block of code
# This next code block MUST be at the very bottom of your program.
# Leave everthing below this line alone!
# --------------------------------

# I've called main() for you.
# This line is a special way to call main
# that allows me to test your code.  Do not change it!
if __name__ == '__main__':
    main()
