# 4-1. Pizzas: 
# Think of at least three kinds of your favorite pizza. 
# Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza.
# For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# • Add a line at the end of your program, outside the for loop, that states how much you like pizza.
# He output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, 
# such as I really love pizza!

favorite_pizzas = ['New York-style pizza', 'Milano Pizza', 'Okonomiyaki pizza']
for pizza in favorite_pizzas:
    print(pizza)
for pizza in favorite_pizzas:
    print(f"{pizza.upper()}, My favorite food!")
print("\nI really love Pizza!")

# 4-2. Animals:
# Think of at least three different animals that have a common characteristic. 
# Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# • Modify your program to print a statement about each animal, such as A dog would make a great pet.
# • Add a line at the end of your program, stating what these animals have in common. 
# You could print a sentence, such as Any of these animals would make a great pet!

animals = ['Wolf', 'Dog', 'Cat']
for animal in animals:
    print(animal)
for animal in animals:
    print(f"{animal.upper()}, is Carnivorous!")
print("\nAll of these animals eat meat!")
