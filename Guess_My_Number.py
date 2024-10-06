import random
import arcade


def guess_My_Number(name = "PlayerOne"):
    game_Count =0
    player_wins =0
    python_wins =0

    def play_Game():
        print(" ")
        player_Choise = input(f"{name} Guess Which Number I'm Thinking Of... 1,2 or 3\n")
        player = int(player_Choise)

        if(player_Choise not in ["1","2","3"]):
            print("You must enter 1,2 or 3")
            return play_Game()

        computer_Choise = random.choice("123")
        computer = int(computer_Choise)


        print(" ")
        def gamePlay(player,computer): 
              nonlocal python_wins
              nonlocal player_wins
              nonlocal name
              if player != computer:
                python_wins+=1
                print(f" {name} you chose {player}\nI was thinking about number {computer}\n sorry {name} BetterLuck NextTime!")
              else:
                player_wins +=1
                print(f" {name} you chose {player}\nI also think number {computer}\n both thinking are same nice Play Congrats {name} You Win!")
        gamePlay(player,computer)

        nonlocal game_Count
        game_Count+=1

        print(f"Game_Count:{str(game_Count)}")

        print(f"\n{name}'s wins:{str(player_wins)}")

        print(f"\nPython wins:{str(python_wins)}")

        print(f"Your Winning Percentage {player_wins/game_Count:.2%}")

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
            arcadeStart = arcade.arcade(name)
            arcadeStart()
            
            

    return play_Game

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
    guess_My_Number_Game = guess_My_Number(args.name)
    guess_My_Number_Game()



