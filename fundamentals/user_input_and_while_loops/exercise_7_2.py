# 7-4. Pizza Toppings:
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
# As they enter each topping, print a message saying you’ll add that topping to their pizza.

active = True
while active:
    user_topping = input("\nPlease type the topping you want to add: (or 'quit' to finish): ").lower()
    if user_topping == 'quit':
        active = False
    else:
        print(f"The {user_topping.title()} is added to your pizza.")

# 7-5. Movie Tickets:
# A movie theater charges different ticket prices depending on a person’s age. 
# If a person is under the age of 3, the ticket is free; 
# if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15.
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

active = True
while active:
    print("\nWelcome! (Enter 'quit' to exit)")
    user_input = input("Please enter your age: ")
    
    if user_input.lower() == 'quit':
        active = False
        continue
        
    user_age = int(user_input)
    if user_age < 3:
        print("The ticket is free.")
    elif 3 <= user_age <= 12:
        print("The ticket is $10.")
    else:
        print("The ticket is $15.")

# 7-6. Three Exits:
# Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.

number_of_people = 0
while number_of_people < 2:
    print("\nWelcome!")
    user_age = int(input("Please Enter your age: "))
    if user_age < 3:
        print("The ticket is free.")
        number_of_people += 1
    elif 3 <= user_age <= 12:
        print("The ticket is $10.")
        number_of_people += 1
    elif user_age > 12:
        print("The ticket is $15.")
        number_of_people += 1

active = True
while active:
    user_topping = input("\nPlease type the topping you want to add: (Enter 'quit' to exit)").lower()
    if user_topping == 'quit':
        active = False
    else:
        print(f"The {user_topping.title()} is added to your pizza.")

while True:
    print("\nWelcome!")
    user_input = input("Please Type 'start' to start the program or 'quit' to finish the program: ").lower()
    if user_input == 'quit':
        break
    elif user_input == 'start':
        user_age = int(input("Please Enter your age: "))
        if user_age < 3:
            print("The ticket is free.")
        elif 3 <= user_age <= 12:
            print("The ticket is $10.")
        elif user_age > 12:
            print("The ticket is $15.")

# 7-7. Infinity:
# Write a loop that never ends, and run it. 
# (To end the loop, press CTRL-C or close the window displaying the output.)

number = 10
while number < 20:
    print(number)

