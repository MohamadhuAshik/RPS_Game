from enum import Enum
import RPS_Game
import Guess_My_Number
import sys

class Arcade(Enum):
    Rock_Paper_Scissor =1
    Guess_My_Number =2

def arcade(name):
    def gamePlay():
        print("")
        userInput =  input(f"{name} welcome to the argade\nplease choose a game...\n1 for Rock_Paper_Scissor\n2 for Guess_My_Number\n\nor press x to exit the arcade\n")
        if(userInput not in ["1","2","x"]):
            print("You must enter 1,2")
            return gamePlay()
        
        if userInput == "1":
            playGame = RPS_Game.rps(name)
            playGame()
        elif userInput =="x":
               print("\n🎉🎉🎉")
               print(f"Thanks for playing!{name}\n")
               sys.exit("Bye! 👋")
        else:
            playGame = Guess_My_Number.guess_My_Number(name)
            playGame()

    return gamePlay

        

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
    description="Provides a personalized game experience."
     )

    parser.add_argument(
        '-n', '--name',metavar="name",
        required=True,help="Name Of The Person Greet"
    )

    args = parser.parse_args()
    arcadeStart = arcade(args.name)
    arcadeStart()
