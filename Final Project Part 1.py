# Put your name here: Nadia Schuld

# comments start with the hash.  
# Be sure to read these!

# Don't change this line:
from datetime import datetime

def main():
  banner()
  while True:
    menuValue = menu()
    if menuValue == 1:
      menu()
    elif menuValue == 2: 
      defaultReport()
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
  print('\nMortality Rate Comparison Menu\n\n1.  Show This Menu Again\n2.  Full Mortality Report by State\n3.  Mortality for a Single State, by Date Range\n4.  Mortality Summary for all States\n5.  Exit\n')
  userMenuSelection = int(input('Make your selection from the menu: '))
  while True:
    try:
      userMenuSelection = int(userMenuSelection)
    except:
      print(userMenuSelection,'is not a valid number')
      userMenuSelection = input('Please enter a valid number: ') 
    else:
      return userMenuSelection

def openCDCfile():
  dataFromFile = open('cdc.csv')
  dataLines = dataFromFile.readlines()
  for dataLines in range[0:7]:
    newDataLines = next(dataLines)
  dataFromFile.close
  return dataFromFile
    
  
def defaultReport():
  newFile = open('Full_Mortality_By_State_Report.txt','w')
  
  
  
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   









# Put all of your code ABOVE this block of code
# This next code block MUST be at the very bottom of your program.
# Leave everthing below this line alone!
# --------------------------------

# I've called main() for you.
# This line is a special way to call main
# that allows me to test your code.  Do not change it!
if __name__ == '__main__':
    main()

