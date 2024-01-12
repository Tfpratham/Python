import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SISSORS = 3
    
#rock paper siccor game using python
print('')
playerchoice = input('Enter \n 1:ROCK  \n 2:PAPER \n 3:SISSORS \n\n')

#choice string me hai isliye int me cast kiya hai  
player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("Enter a valid choice B/W 1,2 or 3 ")

computerchoice = random.choice('123')

computer = int(computerchoice)

print('')
print("Tune " + str(RPS(player)).replace('RPS.', '') +  ' liya.')
print('Python ne ' + str(RPS(computer)).replace('RPS.', '') + ' liya.')
print('')

if player == 1 and computer == 3:
    print('🎉 TU JEET GAYA BHAI!!!🎉 ')
elif player == 2 and computer == 1:
    print('🎉 TU JEET GAYA BHAI!!! 🎉')
elif player == 3 and computer == 2:
    print('🎉 TU JEET GAYA BHAI!!! 🎉')
elif player == computer :
    print('😳 KOI NAHI JEETA BHAI 😳')
else:
    print('😢🐍 PYTHON JEET GAYA BHAI 😢🐍')