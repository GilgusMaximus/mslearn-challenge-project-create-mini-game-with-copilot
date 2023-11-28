# The player can choose one of the three options `rock`, `paper`, or `scissors` and should be warned if they enter an invalid option.
# The computer chooses a random option.
# A winner is selected according to the rules of the game and a winning message is printed.
# The player can play again.
# The score is kept and printed after each round.

import random
import os


player_name = input("Welcome to the game! What is your name? ")
print(f"Hi, {player_name}! Let's play Rock, Paper, Scissors!")

# Create a game loop where the player can decide to play or quit.
while True:
    # Create a list of play options
    play_options = ["rock", "paper", "scissors"]

    # Create a variable to store the computer's play
    computer_play = random.choice(play_options)

    # Create a variable to store the player's play
    player_play = input("Please choose one of the following: rock, paper, scissors: ")
    player_play = player_play.lower()

    # Validate the player's play
    while player_play not in play_options:
        print("Invalid input. Please try again.")
        player_play = input("Please choose one of the following: rock, paper, scissors: ")
        player_play = player_play.lower()

    # Create a function to compare the plays
    def compare_plays(player, computer):
        if player == computer:
            return "It's a tie!"
        elif player == "rock":
            if computer == "paper":
                return "You lose!"
            else:
                return "You win!"
        elif player == "paper":
            if computer == "scissors":
                return "You lose!"
            else:
                return "You win!"
        elif player == "scissors":
            if computer == "rock":
                return "You lose!"
            else:
                return "You win!"

    # Print the results of the game
    print(f"You chose {player_play}. The computer chose {computer_play}.")
    print(compare_plays(player_play, computer_play))

    # Ask the player if they want to play again
    play_again = input("Would you like to play again? (y/n) ")
    play_again = play_again.lower()

    # Validate the player's response
    while play_again != "y" and play_again != "n":
        print("Invalid input. Please try again.")
        play_again = input("Would you like to play again? (y/n) ")
        play_again = play_again.lower()

    # If the player chooses to quit, exit the game
    if play_again == "n":
        print("Thanks for playing! Goodbye!")
        break
    # If the player chooses to play again, clear the terminal and continue the game loop
    elif play_again == "y":
        os.system("clear")
        continue