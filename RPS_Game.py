import random
import sys
from enum import Enum
import arcade

class RPS(Enum):
    ROCK = 1
    PAPER= 2
    SCISSOR = 3


def rps(name = "Player One"):
    game_Count =0
    player_wins =0
    python_wins =0

    def play_Game():
        print(" ")
        player_Choise = input(f"{name} Enter.......\n\n1 for Rock\n2 for paper\n3 for scissor\n\n")
        player = int(player_Choise)

        if(player_Choise not in ["1","2","3"]):
            print("You must enter 1,2 or 3")
            return play_Game()

        computer_Choise = random.choice("123")
        computer = int(computer_Choise)


        print(" ")

        print(f"{name} you Choise :{str(RPS(player)).replace("RPS.","")}")
        print(f"computer_Choise :{str(RPS(computer)).replace("RPS.","")}")

        def game_Play(player,computer):
            print(" ")
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if(player==1 and computer==3):
                player_wins+=1
                print(f"🎉 {name} You Win!")
            elif(player==2 and computer==1):
                player_wins+=1
                print(f"🎉 {name} You Win!")
            elif(player==3 and computer==2):
                player_wins+=1
                print(f"🎉 {name} You Win!")
            elif(player == computer):
                print(f"{name} No One Win 😑 tie Game!")
            else:
                python_wins+=1
                print(f"sorry {name} 🐍 Python Win!")

        game_Play(player,computer)
        print("")
        nonlocal game_Count
        game_Count+=1
        print(f"Game_Count:{str(game_Count)}")
        print(f"\n{name}'s wins:{str(player_wins)}")
        print(f"\nPython wins:{str(python_wins)}")
        print("\nPlay Again? ")

        while True:
            playAgain = input(f"\n{name}\nY for yes\nQ for Quit\n\n")
            if playAgain.lower() not in ["y","q"]:
                continue
            else:
                break
        
        
        if playAgain == "y":
            return play_Game()
        else:
            arcadeStart=arcade.arcade(name)
            arcadeStart()
          
            

    return play_Game


if __name__ =="__main__":
    import argparse

    parser = argparse.ArgumentParser(
    description="Provides a personalized game experience."
     )

    parser.add_argument(
        '-n', '--name',metavar="name",
        required=True,help="Name Of The Person Greet"
    )

    args = parser.parse_args()
    play_Rock_Paper_Scissor = rps(args.name)
    play_Rock_Paper_Scissor()