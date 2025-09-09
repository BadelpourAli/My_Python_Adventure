# 7-1. Rental Car:
# Write a program that asks the user what kind of rental car they would like. 
# Print a message about that car, such as “Let me see if I can find you a Subaru.”

user_favorite_car = input(f"\nTell me your favorite car: ").upper()
print(f"\nOk, cool. I'll check right now to see if I have a {user_favorite_car} or not.")

# 7-2. Restaurant Seating:
# Write a program that asks the user how many people are in their dinner group. 
# If the answer is more than eight, print a message saying they’ll have to wait for a table. 
# Otherwise, report that their table is ready.

user_number_of_people = int(input("\nHow many people are you in your dinner group? "))
if user_number_of_people > 8:
    print("Sorry, you will have to wait for a table.")
else:
    print("Your table is ready.")

# 7-3. Multiples of Ten:
# Ask the user for a number, and then report whether the number is a multiple of 10 or not.

user_number = int(input("\nEnter a number to check that is that number is a multiple of 10 or not: "))
if user_number % 10 == 0:
    print(f"The number {user_number} is a multiple of 10.")
else:
    print(f"The number {user_number} is not a multiple of 10.")

