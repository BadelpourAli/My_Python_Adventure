# 5-1. Conditional Test: 
# Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. 
# Your code should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line evaluates to True or False.
# • Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

language = 'English'
print("\nIs language == 'English'? I predict True.")
print(language == 'English')
print("Is language == 'Russian'? I predict False.")
print(language == 'Russian')
food = 'Pizza'
print("\nIs food == 'Pizza'? I predict True.")
print(food == 'Pizza')
print("Is food == 'Hamburger'? I predict False.")
print(food == 'Hamburger')
car = 'Lambo'
print("\nIs car == 'Lambo'? I predict True.")
print(car == 'Lambo')
print("Is car == 'BMW'? I predict False.")
print(car == 'BMW')
game = 'Chess'
print("\nIs game == 'Chess'? I predict True.")
print(game == 'Chess')
print("Is game == 'Football'? I predict False.")
print(game == 'Football')
color = 'Blue'
print("\nIs color == 'Blue'? I predict True.")
print(color == 'Blue')
print("Is color == 'Red'? I predict False.")
print(color == 'Red')

# 5-2. More Conditional Tests: 
# You don’t have to limit the number of tests you create to 10. 
# If you want to try more comparisons, write more tests and add them to conditional_tests.py. 
# Have at least one True and one False result for each of the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, greater than and less 
# than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

message = 'Hello'
print(f"\nThe answer I predict is Flase: {message == 'hello'}")
print(f"\nThe answer I predict is True: {message == 'Hello'}")
print(f"\nThe answer I predict is True: {message.lower() == 'hello'}")
number = 9
print(f"\nThe answer is True. Let's see: {number == 9}")
print(f"\nThe answer is False. Let's see: {number == 10}")
print(f"\nThe answer is True. Let's see: {number > 5}")
print(f"\nThe answer is Flase. Let's see: {number < 5}")
print(f"\nThe answer is True. Let's see: {number >= 9} ")
print(f"\nThe answer is True. Let's see: {number <= 9}")
print(f"\nThe answer is True. Let's see: {number < 10 and number > 5}")
print(f"\nThe answer is False. Let's see: {number < 8 or number > 20}")
print(f"\nThe answer is True. Let's see: {number < 10 or number > 100}")
names = ['Jack', 'Sara']
print(f"\nChecking name 'Jack' is in the list or not.\nThe name is in the list, so the answer is True: {'Jack' in names}")
print(f"\nChecking name 'David' is in the list or not.\nThe name is in the list, so the answer is not Flase: {'David' in names}")
