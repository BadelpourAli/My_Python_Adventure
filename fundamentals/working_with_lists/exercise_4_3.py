# 4-10. Slices:
# Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# • Print the message The first three items in the list are: 
# Then use a slice to print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. 
# Then use a slice to print three items from the middle of the list.
# • Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

odd_numbers = []
for number in range(1, 21, 2):
    odd_numbers.append(number)
print(f"\nThis is the odd numbers from 1 to 20: {odd_numbers}")
print(f"\nThe first three items in the list are: {odd_numbers[:3]}")
print(f"\nThree items from the middle of the list are: {odd_numbers[3:6]}")
print(f"\nThe last three items in the list are: {odd_numbers[-3:]}")

# 4-11. My Pizza, Your Pizza:
# Start with your program from Exercise 4-1.  
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite pizzas are:, 
# and then use a for loop to print the first list. 
# Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.

favorite_pizzas = ['New York-style pizza', 'Milano Pizza', 'Okonomiyaki pizza']
for pizza in favorite_pizzas:
    print(pizza)
for pizza in favorite_pizzas:
    print(f"{pizza.upper()}, My favorite food!")
print("\nI really love Pizza!")
friend_pizza = favorite_pizzas[:]
favorite_pizzas.append('Sicilian pizza')
friend_pizza.append('California-style pizza')
print(f"The original list: {favorite_pizzas}")
print(f"The new pizza list: {friend_pizza}")
print("\nMy favorite pizzas are:")
for pizza in favorite_pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza)

# 4-12. More Loops: 
# All versions of foods.py in this section have avoided using for loops when printing, to save space. 
# Choose a version of foods.py, and write two for loops to print each list of foods.

# Note: The task 4-12, is done in 4-11.
