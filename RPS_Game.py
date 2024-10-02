import random
import sys
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER= 2
    SCISSOR = 3


def rps():
    game_Count =0
    player_wins =0
    python_wins =0

    def play_Game():
        print(" ")
        player_Choise = input("Enter.......\n\n1 for Rock\n2 for paper\n3 for scissor\n\n")
        player = int(player_Choise)

        if(player_Choise not in ["1","2","3"]):
            print("You must enter 1,2 or 3")
            return play_Game()

        computer_Choise = random.choice("123")
        computer = int(computer_Choise)


        print(" ")

        print(f"player_Choise :{str(RPS(player)).replace("RPS.","")}")
        print(f"computer_Choise :{str(RPS(computer)).replace("RPS.","")}")

        def game_Play(player,computer):
            print(" ")
            nonlocal player_wins
            nonlocal python_wins
            if(player==1 and computer==3):
                player_wins+=1
                print("🎉 You Win!")
            elif(player==2 and computer==1):
                player_wins+=1
                print("🎉 You Win!")
            elif(player==3 and computer==2):
                player_wins+=1
                print("🎉 You Win!")
            elif(player == computer):
                print("😑 tie Game!")
            else:
                python_wins+=1
                print("🐍 Python Win!")

        game_Play(player,computer)
        print("")
        nonlocal game_Count
        game_Count+=1
        print(f"Game_Count:{str(game_Count)}")
        print(f"\nPlayer wins:{str(player_wins)}")
        print(f"\nPython wins:{str(python_wins)}")
        print("\nPlay Again? ")

        while True:
            playAgain = input("\nY for yes\nQ for Quit\n\n")
            if playAgain.lower() not in ["y","q"]:
                continue
            else:
                break
        
        
        if playAgain == "y":
            return play_Game()
        else:
            print("\n🎉🎉🎉")
            print("Thanks for playing!\n")
            sys.exit("Bye! 👋")
            

    return play_Game

play = rps()
play()