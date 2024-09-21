import random
import sys
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER= 2
    SCISSOR = 3

print(" ")
player_Choise = input("Enter.......\n\n1 for Rock\n2 for paper\n3 for scissor\n\n")
player = int(player_Choise)

if(player<0 or player>3):
    sys.exit("You must enter 1,2 or 3")

computer_Choise = random.choice("123")
computer = int(computer_Choise)


print(" ")

print("player_Choise :"+" " +str(RPS(player)).replace("RPS.",""))
print("computer_Choise :"+" " +str(RPS(computer)).replace("RPS.",""))

print(" ")
if(player==1 and computer==3):
    print("🎉 You Win!")
elif(player==2 and computer==1):
     print("🎉 You Win!")
elif(player==3 and computer==2):
     print("🎉 You Win!")
elif(player == computer):
    print("😑 tie Game!")
else:
    print("🐍 Python Win!")

print(" ")