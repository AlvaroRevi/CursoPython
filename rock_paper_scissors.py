import random

# ASCII art for Rock, Paper, Scissors
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# List to hold the game images
game_images = [rock, paper, scissors]

# --- Game Loop ---
play_again = 'y'
while play_again.lower() == 'y':

    # --- Round Loop (Handles Draws) ---
    while True:
        # Get user choice
        try:
            user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
            # Validate input
            if user_choice < 0 or user_choice > 2:
                print("Invalid number, you lose!")
                # We can end the round here or let the computer play anyway
                # For now, let's just restart the round prompt
                continue 
            print("Your choice:")
            print(game_images[user_choice])
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")
            continue # Go back to the start of the round loop

        # Generate computer choice
        computer_choice = random.randint(0, 2)
        print("PC choice:")
        print(game_images[computer_choice])

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a draw! Let's play the round again.")
            # Continue in the inner loop to replay the round
        else:
            # Check winning conditions for the user
            if (user_choice == 0 and computer_choice == 2) or \
               (user_choice == 1 and computer_choice == 0) or \
               (user_choice == 2 and computer_choice == 1):
                print("You win!")
            else:
                print("You lose!")
            break # Exit the round loop as there's a winner or loser

    # Ask to play again
    play_again = input("Do you want to play another game? (y/n): ")
    if play_again.lower() != 'y':
        print("Thanks for playing!")
        break # Exit the main game loop
