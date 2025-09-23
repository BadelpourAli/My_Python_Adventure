#Dice Roller Program in Python

# Importing Random Module

import random

# Using print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518") to have these shapes:
# ● ┌ ─ ┐ │ └ ┘

# Using these Shapes to Create ASCII Art of Dice.

# Sample
"┌──────────┐"
"│          │"
"│     ●    │"
"│          │"
"└──────────┘"

# Defining the Dice
dice_art ={
    1: (
"┌──────────┐",
"│          │",
"│     ●    │",
"│          │",
"└──────────┘"),

    2: (
"┌──────────┐",
"│ ●        │",
"│          │",
"│        ● │",
"└──────────┘"),
    
    3: (
"┌──────────┐",
"│ ●        │",
"│     ●    │",
"│         ●│",
"└──────────┘"),

    4: (
"┌──────────┐",
"│ ●       ●│",
"│          │",
"│ ●       ●│",
"└──────────┘"),
    
    5: (
"┌──────────┐",
"│ ●       ●│",
"│     ●    │",
"│ ●       ●│",
"└──────────┘"),

    6: (
"┌──────────┐",
"│ ●   ●   ●│",
"│          │",
"│ ●   ●   ●│",
"└──────────┘")
}

# Greeting Message
print("Welcome to the Dice Roller Program in Python!")

# Defining Repeat out side of Main Loop
repeat = True

# Main Loop
while repeat:
    
    # Defining the Status
    dice = []
    total = 0
    
    # Getting the Number of Dice
    number_of_dice = input("How many dice?: ")
    if not number_of_dice.isdigit() or int(number_of_dice) <= 0:
        print("Please type a valid number!")
        continue
    number_of_dice = int(number_of_dice)
    
    # Maximum Dice Limit
    if number_of_dice > 10:  
        print("That's too many dice! Try 10 or fewer.")
        continue
    
    # Getting the Mode of output file
    mode = input("Do you like your dice in Vertical or Horizontal shape? (v/h): ").lower()
    while mode not in ['v', 'h']:
        print("Please enter 'v' for vertical or 'h' for horizontal!")
        mode = input("Do you like your dice in Vertical or Horizontal shape? (v/h): ").lower()

    # Storing random Shapes of Dice in Dice Dictionary
    for die in range(number_of_dice):
        dice.append(random.randint(1, 6))
    
    # Vertical Mode
    if mode == 'v':
        for die in range(number_of_dice):
            for line in dice_art.get(dice[die]):
                print(line)
    
    # Horizontal Mode
    else:
        for line in range(5):
            for die in dice:
                print(dice_art.get(die)[line], end=" ")
            print()

    # Calculating the Total
    for die in dice:
        total += die
    print(f"Total: {total}")

    # Repeat Mode
    while True:
        repeat_input = input("Do you want to Play Again? (y/n)\n>").lower()
        if repeat_input == 'n':
            repeat = False
            break
        elif repeat_input == 'y':
            repeat = True
            break
        else:
            print("Please Enter Y or N.")

print("Thank You for Playing.")
