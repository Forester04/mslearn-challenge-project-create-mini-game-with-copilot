# Python Minigame: Rock, Paper, Scissors
# The game logic follows these rules:
# - Rock beats scissors.
# - Scissors beat paper.
# - Paper beats rock.

# Specifications:
# - The game should be multiplayer, where the computer randomly chooses rock, paper, or scissors.
# - The player can choose rock, paper, or scissors and should be warned if they enter an invalid option.
# - At each round, the player must enter one of the options and be informed if they won, lost, or tied with the computer.
# - The player can choose whether to play again at the end of each round.
# - Display the player's score at the end of the game.
# - The game must handle user inputs, putting them in lowercase and informing the user if the option is invalid.


import random
def play_game():
    options = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    while True:
        # Get player's choice
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        # Validate player's choice
        if player_choice not in options:
            print("Invalid option. Please choose rock, paper, or scissors.")
            continue

        # Generate computer's choice
        computer_choice = random.choice(options)

        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            print("You won!")
            player_score += 1
        else:
            print("You lost!")
            computer_score += 1

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    # Display the final scores
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

play_game()