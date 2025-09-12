#Python Quiz Game
# Welcome message
print("""
    Welcome to the Python Quiz Game!
    Type 'h' for Help!
""")

# Initialize game data
quiz_questions = []
player_score = 0

# Main game loop
while True:
    user_choice = input("|---- Main Menu ----| \n> ")
    
    # Help menu
    if user_choice.lower() == 'h':
        print("""
        Type:
              'r' to run the game.
              'w' to write the questions.
              'a' to see the answers.
              's' to see the score.
              'rs' to reset the score.
              'e' to exit the program.
        """)
    
    # Exit program
    elif user_choice.lower() == 'e':
        print("Thank you for playing!")
        break    
    
    # Quiz creation mode
    elif user_choice.lower() == 'w':
        print("|---- Quiz generation mode ----|")
        
        while True:
            creation_mode = input("Please select the mode: 'g' (generating mode) 'e' (exit):> ")
            
            # Exit quiz creation
            if creation_mode.lower() == 'e':
                print("Back to the main menu:")
                break
            
            # Question generation
            elif creation_mode.lower() == 'g':
                print("\n|---- Making Questions ----|")
                
                question_count = int(input("How many questions do you want to add? \n> "))
                
                for question_index in range(question_count):
                    question_text = input(f"\nEnter question {question_index + 1}:> ")
                    correct_answer = input(f"What is the answer to question {question_index + 1}: ")
                    option_count = int(input(f"How many options for question {question_index + 1}? > "))
                    
                    option_list = []
                    for option_index in range(option_count):
                        option_text = input(f"Enter option {option_index + 1}: ")
                        option_list.append(option_text)
                    
                    question_data = {
                        'question': question_text,
                        'options': option_list,
                        'answer': correct_answer
                    }
                    
                    quiz_questions.append(question_data)
                
                print("\nQuestions added successfully!")
            
            # Invalid mode selection
            else:
                print(f"The '{creation_mode}' is not a valid mode!")
    
    # Run the quiz game
    elif user_choice.lower() == 'r':
        if not quiz_questions:
            print("The quiz list is empty! Please add questions first using 'w'.")
        else:
            print("|---- Running Game ----|")
            print("\nList of questions and options:")
            
            # Reset score for new game
            current_game_score = 0
            
            # Display and process each question
            for question_number, current_question in enumerate(quiz_questions, 1):
                print(f"\n{question_number}. {current_question['question']}")
                
                # Display all options
                for option_number, current_option in enumerate(current_question['options'], 1):
                    print(f"    {option_number}. {current_option}")
                
                # Get and validate user's answer
                user_answer = input(f"Your answer for question {question_number}: ")
                
                # Check if answer is correct
                if user_answer.lower() == current_question['answer'].lower():
                    print('Correct! Well done.')
                    current_game_score += 1
                else:
                    print(f"Sorry, that's incorrect. The correct answer was: {current_question['answer']}")
            
            # Update overall score
            player_score = current_game_score
            print(f"\nQuiz completed! Your score: {player_score}/{len(quiz_questions)}")
    
    # Display current score
    elif user_choice.lower() == 's':
        print(f"Your current score is: {player_score}")
    
    # Reset score
    elif user_choice.lower() == 'rs':
        print("Score has been reset!")
        player_score = 0
    
    # Show all correct answers
    elif user_choice.lower() == 'a':
        if not quiz_questions:
            print("No questions and answers yet!")
        else: 
            print("\nCorrect Answers:")
            for question_number, current_question in enumerate(quiz_questions, 1):
                print(f"{question_number}. {current_question['question']}")
                print(f"   The correct answer is: {current_question['answer']}")
                print()
    
    # Handle invalid input
    else:
        print(f"The command '{user_choice}' is not recognized! \nType 'h' for Help!")