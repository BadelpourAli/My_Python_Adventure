#Python Number Guessing Game
import random
import math

# Initialize game variables
total_guesses = 0
games_won = 0
games_lost = 0

print("---- Welcome to the Number Guessing Game ----")
print("""
Available commands:
      'h' for help.
      's' to start a new game.
      'r' to see your results.
      'e' to exit the program.
      """)

while True:
    user_command = input("---- Main Menu ---- \n> ")
    
    if user_command.lower() == 'h':
        print("""
Available commands:
      'h' for help.
      's' to start a new game.
      'r' to see your results.
      'e' to exit the program.
      
In this game, you define a range of numbers, and I'll select a secret number from that range.
The number of attempts you get depends on the size of your range - larger ranges give you more attempts!
      """)
    
    elif user_command.lower() == 'e':
        print("---- Thank you for playing ----")
        break
    
    elif user_command.lower() == 'r':
        print(f"Total guesses made: {total_guesses}")
        print(f"Games won: {games_won}")
        print(f"Games lost: {games_lost}")
    
    elif user_command.lower() == 's':
        print("Please define a range of numbers. I'll select a secret number from this range!")
        
        # Get and validate the range
        range_start = input("The range starts from: ")
        range_end = input("The range ends at: ")
        
        # Check if inputs are numbers
        if range_start.isdigit() and range_end.isdigit():
            range_start = int(range_start)
            range_end = int(range_end)
            
            # Ensure the range is valid
            if range_start < range_end:
                range_size = range_end - range_start + 1
                print(f"Your range is from {range_start} to {range_end}")
                
                # Calculate attempts based on range size
                # Using log2 of the range size gives a fair number of attempts
                # Minimum 3 attempts, maximum 20 attempts
                attempts_allowed = max(3, min(20, int(math.log2(range_size) * 2) + 1))
                print(f"Based on your range size, you get {attempts_allowed} attempts!")
                
                secret_number = random.randint(range_start, range_end)
                print("I've selected a secret number from your range!")
                
                # Game loop
                for attempt in range(1, attempts_allowed + 1):
                    valid_input = False
                    while not valid_input:
                        user_guess = input(f"Attempt {attempt}/{attempts_allowed} > ")
                        
                        # Check if guess is a number
                        if user_guess.isdigit():
                            user_guess = int(user_guess)
                            valid_input = True
                            
                            # Check if guess is within range
                            if user_guess < range_start or user_guess > range_end:
                                print(f"Your guess must be between {range_start} and {range_end}")
                                valid_input = False
                        else:
                            print("Please enter a valid number.")
                    
                    # Only process the guess if it's valid
                    if valid_input:
                        total_guesses += 1
                        
                        if user_guess < secret_number:
                            print("Too low!")
                        elif user_guess > secret_number:
                            print("Too high!")
                        else:
                            print("Congratulations! You found the secret number!")
                            games_won += 1
                            break
                
                # Check if all attempts were used without guessing correctly
                if user_guess != secret_number:
                    print(f"Sorry, you didn't guess the number. It was {secret_number}.")
                    games_lost += 1
            else:
                print("Error: The start of the range must be less than the end.")
        else:
            print("Error: Please enter valid numbers.")
    
    else:
        print("Invalid command. Type 'h' for available commands.")