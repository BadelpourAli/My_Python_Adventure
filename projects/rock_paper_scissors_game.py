#Rock✊, Scissors✌️, Paper✋ Game in Python!

# Importing Modules
import random
import getpass

# Welcome Message
print("Welcome to Rock ✊, Paper ✋, scissors ✌️ Game in Python! ")

# Defining Status
choices_emoji = {
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌️"
}
win_conditions = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}
history_solo = []
history_co_op = []
solo = False
competitive_mode_Solo = False
user_score = 0
user_score_comp = 0
computer_score = 0
computer_score_comp = 0
co_op = False
competitive_mode_coop = False
user1_score = 0
user1_score_comp = 0
user2_score = 0
user2_score_comp= 0

# Main Menu
while True:
    print("""
---- Main Menu ----
(Type 'help' for help.)
---- --------- ----
""")
    user_input = input("> ")
    
    # Help Command
    if user_input.lower() == 'help':
        print("""
Type:
    'help' for Help.
    'run' to Run the Game in Solo Mode.
    'coop' to Run the Game in Co-op Mode.
    'compsolo' to Run Competitive Mode (Solo)
    'compcoop' to Run Competitive Mode (Co-op)
    'history' to See the History of the Game.
    'scores' to See the Scores.
    'clearh' to Clear the Game History.
    'clears' to Clear the Solo Mode Scores.
    'clearc' to Clear the Co-op Mode Scores.
    'info' to see the Game Info.
    'exit' to Exit the Game.              
""")
    
    # History of the Game
    elif user_input.lower() == 'history':
        if not history_solo:
            print("\nNo solo game history!")
        else:
           print("\nLast 5 games in solo mode:")
        for i, game in enumerate(history_solo[-5:], 1):
            result_icon = "✅" if game["result"] == "win" else "❌" if game["result"] == "loss" else "➖"
            print(f"{i}. You: {choices_emoji[game['user']]} vs PC: {choices_emoji[game['computer']]} {result_icon}")

        if not history_co_op:
            print("\nNo co-op game history!")
        else:
           print("\nLast 5 games in co-op mode:")
        for i, game in enumerate(history_co_op[-5:], 1):
            result_icon = "User 1✅" if game["result"] == "user 1 win" else "User 2✅" if game["result"] == "user 2 win" else "➖"
            print(f"{i}. User 1: {choices_emoji[game['user 1']]} vs User 2: {choices_emoji[game['user 2']]} \n{result_icon}")

    # Running the Game in Solo Mode    
    elif user_input.lower() == 'run':
        print("---- Solo Mode ----")
        solo = True
        while solo:
            choices = ["rock", "paper", "scissors"]
            user_choice = input("\nChoose (rock, paper, scissors or 'e' to exit): ").lower()
            computer_choice = random.choice(choices)
            if user_choice == 'e':
                print("Returning to main menu.")
                solo = False
                break   
            if user_choice in choices:
                result = None
                result = print(""f"\nYou chose: {choices_emoji[user_choice]} {user_choice} \nComputer chose: {choices_emoji[computer_choice]} {computer_choice}""")
                if user_choice == computer_choice:
                    result = 'tie'
                    print("It's a tie.")
                elif win_conditions[user_choice] == computer_choice:
                    result = 'win'
                    user_score += 1
                    print("\nYou won!")
                else:
                    result = 'loss'
                    computer_score += 1
                    print("\nYou lost!")
                history_solo.append({
                "user": user_choice,
                "computer": computer_choice,
                "result": result
                })
            else:
                print("Invalid choice! Please choose rock, paper, or scissors.")
    
    # Running the Game in Co-op Mode
    elif user_input == 'coop':
        print("---- Co-op Mode ----")
        co_op = True
        while co_op:
            choices = ["rock", "paper", "scissors"]
            user1_choice = getpass.getpass("\nUser 1 Choose (rock, paper, scissors or 'e' to exit): ").lower()
            user2_choice = getpass.getpass("User 2 Choose (rock, paper, scissors or 'e' to exit): ").lower()
            if user1_choice == 'e' or user2_choice == 'e':
                print("Returning to main menu.")
                co_op = False
                break   
            if user1_choice in choices and user2_choice in choices:
                result = None
                result = print(""f"\nUser 1 chose: {choices_emoji[user1_choice]} {user1_choice} \nUser 2 chose: {choices_emoji[user2_choice]} {user2_choice}""")
                if user1_choice == user2_choice:
                    result = 'tie'
                    print("It's a tie.")
                elif win_conditions[user1_choice] == user2_choice:
                    result = 'user 1 win'
                    user1_score += 1
                    print("\nUser 1 won!")
                else:
                    result = 'user 2 win'
                    user2_score += 1
                    print("\nUser 2 won!")
                history_co_op.append({
                "user 1": user1_choice,
                "user 2": user2_choice,
                "result": result
                })
            else:
                print("Invalid choice! Please choose rock, paper, or scissors.")        

    # Running Competitive Mode (Solo)
    elif user_input.lower() == 'compsolo':
        print("---- Competitive Mode (Solo) ----")
        competitive_mode_Solo = True
        move_counts_solo = 0
        while competitive_mode_Solo:
            if user_score_comp > computer_score_comp:
                print("\nYou Won The Competition! 😎")
                user_score_comp = 0
                computer_score_comp = 0
            elif computer_score_comp > user_score_comp:
                print("\nComputer Won The Competition! 🤖")
                user_score_comp = 0
                computer_score_comp = 0
            elif move_counts_solo > 0 and user_score_comp == computer_score_comp:
                print("\nThe Competition Is Draw! 😶")
                user_score_comp = 0
                computer_score_comp = 0
            choices = ["rock", "paper", "scissors"]
            rounds = 1
            current_round = 0
            user_input_compsolo = input("How many rounds would you like to play? \n(Type 'exit' to get back to Main Menu) \n>")
            if user_input_compsolo.isdigit():
                rounds_play = int(user_input_compsolo)
                while rounds_play >= rounds:
                    user_choice = input("\nChoose (rock, paper, scissors or 'e' to exit): ").lower()
                    computer_choice = random.choice(choices)
                    if user_choice == 'e':
                        print("Returning to main menu.")
                        competitive_mode_Solo = False
                        break   
                    elif user_choice in choices:
                        result = None
                        result = print(""f"\nYou chose: {choices_emoji[user_choice]} {user_choice} \nComputer chose: {choices_emoji[computer_choice]} {computer_choice}""")
                        if user_choice == computer_choice:
                            result = 'tie'
                            rounds += 1
                            current_round += 1
                            move_counts_solo += 1
                            print("It's a tie.")
                            print(f"Round {current_round} finished!")
                        elif win_conditions[user_choice] == computer_choice:
                            result = 'win'
                            user_score += 1
                            user_score_comp += 1
                            rounds += 1
                            current_round += 1
                            move_counts_solo += 1
                            print(f"Round {current_round} finished!")
                            print("\nYou won!")
                        else:
                            result = 'loss'
                            computer_score += 1
                            rounds += 1
                            computer_score_comp += 1
                            current_round += 1
                            move_counts_solo += 1
                            print(f"Round {current_round} finished!")
                            print("\nYou lost!")
                        history_solo.append({
                        "user": user_choice,
                        "computer": computer_choice,
                        "result": result
                        })
                    else:
                        print("Invalid choice! Please choose rock, paper, or scissors.")
            elif user_input_compsolo.lower() == 'exit':
                print("Getting back to Main Menu")
                competitive_mode_Solo = False
                break
            else:
                print("Invalid Command!")
    
    # Running Competitive Mode (Co-op)
    elif user_input.lower() == 'compcoop':
        print("---- Competitive Mode (Co-op) ----")
        competitive_mode_coop = True
        move_counts_coop = 0
        while competitive_mode_coop:
            if user1_score_comp > user2_score_comp:
                print("\nUser 1 Won The Competition! 😊")
                user1_score_comp = 0
                user2_score_comp = 0
            elif user2_score_comp > user1_score_comp:
                print("\nUser 2 Won The Competition! 😀")
                user1_score_comp = 0
                user2_score_comp = 0
            elif move_counts_coop > 0 and user1_score_comp == user2_score_comp:
                print("\nThe Competition Is Draw! 😶")
                user1_score_comp = 0
                user2_score_comp = 0
            choices = ["rock", "paper", "scissors"]
            rounds = 1
            current_round = 0
            users_input_coop = input("How many rounds would you like to play? \n(Type 'exit' to get back to Main Menu) \n>")
            if users_input_coop.isdigit():
                rounds_play = int(users_input_coop)
                while rounds_play >= rounds:
                    user1_choice = getpass.getpass("\nUser 1 Choose (rock, paper, scissors or 'e' to exit): ").lower()
                    user2_choice = getpass.getpass("User 2 Choose (rock, paper, scissors or 'e' to exit): ").lower()
                    if user1_choice == 'e' or user2_choice == 'e':
                        print("Returning to main menu.")
                        competitive_mode_coop = False
                        break   
                    if user1_choice in choices and user2_choice in choices:
                        result = None
                        result = print(""f"\nUser 1 chose: {choices_emoji[user1_choice]} {user1_choice} \nUser 2 chose: {choices_emoji[user2_choice]} {user2_choice}""")
                        if user1_choice == user2_choice:
                            result = 'tie'
                            rounds += 1
                            current_round += 1
                            move_counts_coop += 1
                            print("It's a tie.")
                            print(f"Round {current_round} finished!")
                        elif win_conditions[user1_choice] == user2_choice:
                            result = 'user 1 win'
                            user1_score += 1
                            user1_score_comp += 1
                            rounds += 1
                            current_round += 1
                            move_counts_coop += 1
                            print("\nUser 1 won!")
                            print(f"Round {current_round} finished!")
                        else:
                            result = 'user 2 win'
                            user2_score += 1
                            user2_score_comp += 1
                            rounds += 1
                            current_round += 1
                            move_counts_coop += 1
                            print("\nUser 2 won!")
                            print(f"Round {current_round} finished!")
                        history_co_op.append({
                        "user 1": user1_choice,
                        "user 2": user2_choice,
                        "result": result
                        })
                    else:
                        print("Invalid choice! Please choose rock, paper, or scissors.")
            elif users_input_coop.lower() == 'exit':
                print("Getting back to Main Menu")
                competitive_mode_coop = False
                break
            else:
                print("Invalid Command!")
        
    # Showing Scores
    elif user_input.lower() == 'scores':
        print("\n---- Solo Mode Scores ----")
        print(f"Your score 😎: {user_score}")
        print(f"Computer score 🤖: {computer_score}")
        print("\n---- Co-op Mode Scores ----")
        print(f"User 1 score 😊: {user1_score}")
        print(f"User 2 score 😀: {user2_score}")

    # Clearing Scores in Solo Mode
    elif user_input.lower() == 'clears':
        if user_score == 0 and computer_score == 0:
            print("No scores in Solo Mode yet!")
        else:
            print("Solo Mode scores is cleared!")
            user_score = 0
            computer_score = 0
    
    # Clearing Scores in Co-op Mode:
    elif user_input.lower() == 'clearc':
        if user1_score == 0 and user2_score == 0:
            print("No scores in Co-op Mode yet! ")
        else:
            print("Co-op Mode scores is cleared!")
            user1_score = 0
            user2_score = 0

    # Clearing History of the Game
    elif user_input.lower() == 'clearh':
        if not history_solo:
            print("\nNo solo game history!")
        else:
            history_solo.clear()
            print("Solo history cleared!")
        if not history_co_op:
            print("\nNo co-op game history!")
        else:
            history_co_op.clear()
            print("Co-op history cleared!")

    # Showing Program Info
    elif user_input.lower() == 'info':
        print("\n--- Developed by Ali Badelpour ----")
    
    # Exiting Game
    elif user_input.lower() == 'exit':
        print("---- Thank you for playing! ----")
        break
    
    # Invalid Command 
    else:
        print("Invalid Command! \nType 'help' for help.")