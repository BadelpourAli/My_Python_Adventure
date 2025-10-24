import random
import getpass

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
user_score = 0
user_score_comp = 0
computer_score = 0
computer_score_comp = 0
user1_score = 0
user1_score_comp = 0
user2_score = 0
user2_score_comp = 0

def help():
    print("""
Type:
    'help' for Help.
    'solo' to Run the Game in Solo Mode.
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

def check_winner(choice1, choice2, mode='solo'):
    if choice1 == choice2:
        return 'tie'
    elif win_conditions[choice1] == choice2:
        return 'win' if mode == 'solo' else 'user 1 win'
    else:
        return 'loss' if mode == 'solo' else 'user 2 win'

def get_valid_choice(prompt, hidden=False):
    choice = getpass.getpass(prompt) if hidden else input(prompt)
    return choice.lower()

def display_choices(choice1, choice2, player1_name="You", player2_name="Computer"):
    print(f"\n{player1_name} chose: {choices_emoji[choice1]} {choice1}")
    print(f"{player2_name} chose: {choices_emoji[choice2]} {choice2}")

def display_history(history_list, mode):
    if not history_list:
        print(f"\nNo {mode} game history!")
        return
    
    print(f"\nLast 5 games in {mode} mode:")
    for i, game in enumerate(history_list[-5:], 1):
        if mode == 'solo':
            result_icon = "✅" if game["result"] == "win" else "❌" if game["result"] == "loss" else "➖"
            print(f"{i}. You: {choices_emoji[game['user']]} vs PC: {choices_emoji[game['computer']]} {result_icon}")
        else:
            result_icon = "User 1✅" if game["result"] == "user 1 win" else "User 2✅" if game["result"] == "user 2 win" else "➖"
            print(f"{i}. User 1: {choices_emoji[game['user 1']]} vs User 2: {choices_emoji[game['user 2']]} \n{result_icon}")

def history():
    display_history(history_solo, 'solo')
    display_history(history_co_op, 'co-op')

def solo_mode():
    global user_score, computer_score
    print("---- Solo Mode ----")
    while True:
        user_choice = get_valid_choice("\nChoose (rock, paper, scissors or 'e' to exit): ")
        if user_choice == 'e':
            print("Returning to main menu.")
            break
        
        if user_choice in ["rock", "paper", "scissors"]:
            computer_choice = random.choice(["rock", "paper", "scissors"])
            display_choices(user_choice, computer_choice)
            
            result = check_winner(user_choice, computer_choice, 'solo')
            
            if result == 'win':
                user_score += 1
                print("\nYou won!")
            elif result == 'loss':
                computer_score += 1
                print("\nYou lost!")
            else:
                print("It's a tie.")
            
            history_solo.append({
                "user": user_choice,
                "computer": computer_choice,
                "result": result
            })
        else:
            print("Invalid choice! Please choose rock, paper, or scissors.")

def coop_mode():
    global user1_score, user2_score
    print("---- Co-op Mode ----")
    while True:
        user1_choice = get_valid_choice("\nUser 1 Choose (rock, paper, scissors or 'e' to exit): ", hidden=True)
        user2_choice = get_valid_choice("User 2 Choose (rock, paper, scissors or 'e' to exit): ", hidden=True)
        
        if user1_choice == 'e' or user2_choice == 'e':
            print("Returning to main menu.")
            break
        
        if user1_choice in ["rock", "paper", "scissors"] and user2_choice in ["rock", "paper", "scissors"]:
            display_choices(user1_choice, user2_choice, "User 1", "User 2")
            
            result = check_winner(user1_choice, user2_choice, 'coop')
            
            if result == 'user 1 win':
                user1_score += 1
                print("\nUser 1 won!")
            elif result == 'user 2 win':
                user2_score += 1
                print("\nUser 2 won!")
            else:
                print("It's a tie.")
            
            history_co_op.append({
                "user 1": user1_choice,
                "user 2": user2_choice,
                "result": result
            })
        else:
            print("Invalid choice! Please choose rock, paper, or scissors.")

def play_competitive_rounds(mode, rounds_play):
    global user_score, computer_score, user_score_comp, computer_score_comp
    global user1_score, user2_score, user1_score_comp, user2_score_comp
    
    rounds = 1
    current_round = 0
    move_counts = 0
    
    while rounds_play >= rounds:
        if mode == 'solo':
            user_choice = get_valid_choice("\nChoose (rock, paper, scissors or 'e' to exit): ")
            if user_choice == 'e':
                return False, move_counts
            
            if user_choice in ["rock", "paper", "scissors"]:
                computer_choice = random.choice(["rock", "paper", "scissors"])
                display_choices(user_choice, computer_choice)
                
                result = check_winner(user_choice, computer_choice, 'solo')
                
                if result == 'win':
                    user_score += 1
                    user_score_comp += 1
                    print("\nYou won!")
                elif result == 'loss':
                    computer_score += 1
                    computer_score_comp += 1
                    print("\nYou lost!")
                else:
                    print("It's a tie.")
                
                history_solo.append({
                    "user": user_choice,
                    "computer": computer_choice,
                    "result": result
                })
            else:
                print("Invalid choice! Please choose rock, paper, or scissors.")
                continue
        else:  # coop mode
            user1_choice = get_valid_choice("\nUser 1 Choose (rock, paper, scissors or 'e' to exit): ", hidden=True)
            user2_choice = get_valid_choice("User 2 Choose (rock, paper, scissors or 'e' to exit): ", hidden=True)
            
            if user1_choice == 'e' or user2_choice == 'e':
                return False, move_counts
            
            if user1_choice in ["rock", "paper", "scissors"] and user2_choice in ["rock", "paper", "scissors"]:
                display_choices(user1_choice, user2_choice, "User 1", "User 2")
                
                result = check_winner(user1_choice, user2_choice, 'coop')
                
                if result == 'user 1 win':
                    user1_score += 1
                    user1_score_comp += 1
                    print("\nUser 1 won!")
                elif result == 'user 2 win':
                    user2_score += 1
                    user2_score_comp += 1
                    print("\nUser 2 won!")
                else:
                    print("It's a tie.")
                
                history_co_op.append({
                    "user 1": user1_choice,
                    "user 2": user2_choice,
                    "result": result
                })
            else:
                print("Invalid choice! Please choose rock, paper, or scissors.")
                continue
        
        rounds += 1
        current_round += 1
        move_counts += 1
        print(f"Round {current_round} finished!")
    
    return True, move_counts

def comp_solo():
    global user_score_comp, computer_score_comp
    print("---- Competitive Mode (Solo) ----")
    
    while True:
        if user_score_comp > computer_score_comp:
            print("\nYou Won The Competition! 😎")
            user_score_comp = 0
            computer_score_comp = 0
        elif computer_score_comp > user_score_comp:
            print("\nComputer Won The Competition! 🤖")
            user_score_comp = 0
            computer_score_comp = 0
        
        user_input_compsolo = input("How many rounds would you like to play? \n(Type 'exit' to get back to Main Menu) \n>")
        
        if user_input_compsolo.isdigit():
            rounds_play = int(user_input_compsolo)
            completed, move_counts = play_competitive_rounds('solo', rounds_play)
            
            if not completed:
                break
            
            if move_counts > 0 and user_score_comp == computer_score_comp:
                print("\nThe Competition Is Draw! 😶")
                user_score_comp = 0
                computer_score_comp = 0
        elif user_input_compsolo.lower() == 'exit':
            print("Getting back to Main Menu")
            break
        else:
            print("Invalid Command!")

def comp_coop():
    global user1_score_comp, user2_score_comp
    print("---- Competitive Mode (Co-op) ----")
    
    while True:
        if user1_score_comp > user2_score_comp:
            print("\nUser 1 Won The Competition! 😊")
            user1_score_comp = 0
            user2_score_comp = 0
        elif user2_score_comp > user1_score_comp:
            print("\nUser 2 Won The Competition! 😀")
            user1_score_comp = 0
            user2_score_comp = 0
        
        users_input_coop = input("How many rounds would you like to play? \n(Type 'exit' to get back to Main Menu) \n>")
        
        if users_input_coop.isdigit():
            rounds_play = int(users_input_coop)
            completed, move_counts = play_competitive_rounds('coop', rounds_play)
            
            if not completed:
                break
            
            if move_counts > 0 and user1_score_comp == user2_score_comp:
                print("\nThe Competition Is Draw! 😶")
                user1_score_comp = 0
                user2_score_comp = 0
        elif users_input_coop.lower() == 'exit':
            print("Getting back to Main Menu")
            break
        else:
            print("Invalid Command!")

def show_score():
    print("\n---- Solo Mode Scores ----")
    print(f"Your score 😎: {user_score}")
    print(f"Computer score 🤖: {computer_score}")
    print("\n---- Co-op Mode Scores ----")
    print(f"User 1 score 😊: {user1_score}")
    print(f"User 2 score 😀: {user2_score}")

def clear_score_solo():
    global user_score, computer_score
    if user_score == 0 and computer_score == 0:
        print("No scores in Solo Mode yet!")
    else:
        print("Solo Mode scores is cleared!")
        user_score = 0
        computer_score = 0

def clear_score_coop():
    global user1_score, user2_score
    if user1_score == 0 and user2_score == 0:
        print("No scores in Co-op Mode yet! ")
    else:
        print("Co-op Mode scores is cleared!")
        user1_score = 0
        user2_score = 0

def clear_history():
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

def info():
    print("\n--- Developed by Ali Badelpour ----")

while True:
    print("""
---- Main Menu ----
(Type 'help' for help.)
---- --------- ----
""")

    user_input = input("> ")
    if user_input.lower() == 'help':
        help()
    elif user_input.lower() == 'solo':
        solo_mode()
    elif user_input.lower() == 'coop':
        coop_mode()
    elif user_input.lower() == 'compsolo':
        comp_solo()
    elif user_input.lower() == 'compcoop':
        comp_coop()
    elif user_input.lower() == 'scores':
        show_score()
    elif user_input.lower() == 'clears':
        clear_score_solo()
    elif user_input.lower() == 'clearc':
        clear_score_coop()
    elif user_input.lower() == 'clearh':
        clear_history()
    elif user_input.lower() == 'info':
        info()
    elif user_input.lower() == 'history':
        history()
    elif user_input.lower() == 'exit':
        print("---- Thank you for playing! ----")
        break
    else:
        print("Invalid Command! \nType 'help' for help.")