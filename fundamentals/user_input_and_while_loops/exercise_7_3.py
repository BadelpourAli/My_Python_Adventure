# 7-8. Deli: 
# Make a list called sandwich_orders and fill it with the names of various sandwiches. 
# Then make an empty list called finished_sandwiches. 
# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. 
# As each sandwich is made, move it to the list of finished sandwiches. 
# After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = [
    'Burrata Pizza Sandwiches', 'Sushi Sandwich (Onigirazu)', 'Chopped Sandwich', 'Italian Beef Sandwich', 
    'Best Chicken Salad', 'Tuscan Chicken Wrap', 'Mexican Torta'
    ]
finished_sandwiches = []
print("\nThe orders:\n")
for sandwich_order in sandwich_orders:
    print(sandwich_order.title())
while sandwich_orders:
    current_sandwich =sandwich_orders.pop()
    print(f"\nThe {current_sandwich.title()} is ready!")
    finished_sandwiches.append(current_sandwich)
print("\nFinished Sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

# 7-9. No Pastrami:
# Using the list sandwich_orders from Exercise 7-8, 
# make sure the sandwich 'pastrami' appears in the list at least three times. 
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = [
    'Burrata Pizza Sandwiches', 'Sushi Sandwich (Onigirazu)', 'Chopped Sandwich', 'Italian Beef Sandwich',
    'Pastrami', 'Best Chicken Salad', 'Tuscan Chicken Wrap', 'Pastrami', 'Mexican Torta', 'Pastrami'
    ]
finished_sandwiches = []
print("\nThe orders:\n")
for sandwich_order in sandwich_orders:
    print(sandwich_order.title())
print("\nThe Deli has run out of Pastrami!\n")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
while sandwich_orders:
    current_sandwich =sandwich_orders.pop()
    print(f"The {current_sandwich.title()} is ready!")
    finished_sandwiches.append(current_sandwich)
print("\nFinished Sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

# 7-10. Dream Vacation:
# Write a program that polls users about their dream vacation. 
# Write a prompt similar to If you could visit one place in the world, where would you go? 
# Include a block of code that prints the results of the poll.

responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name?\n")
    dream_vacation = input("If you could visit one place in the world, where would you go? ")

    responses[name] = dream_vacation

    repeat = input("Would you like to let another person respond? (yes/ no) ").lower()
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---\n")

for name, dream_vacation in responses.items():
    print(f"{name.title()} would like to visit {dream_vacation.title()}.")
