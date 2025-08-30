# 3-1. Names:
# Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.

names = ['Sam', 'Sara', 'David', 'Jack']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 3-2. Greetings: 
# Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. 
# The text of each message should be the same, but each message should be personalized with the person’s name.

names = ['sam', 'sara', 'david', 'jack']
message_0 = f"Welcome to the Team {names[0].title()}!"
message_1 = f"Welcome to the Team {names[1].title()}!"
message_2 = f"Welcome to the Team {names[2].title()}!"
message_3 = f"Welcome to the Team {names[3].title()}!"
print(message_0)
print(message_1)
print(message_2)
print(message_3)

# 3-3. Your Own List: 
# Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples.
# Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

my_own_list = ['lamborghini aventador', 'mercedes-amg one', 'koenigsegg jesko', 'nissan 240sx']
car_0 = f"I would like to own a {my_own_list[-1].upper()} car!"
car_1 = f"I would like to own a {my_own_list[0].upper()} car!"
car_2 = f"I would like to own a {my_own_list[1].upper()} car!"
car_3 = f"I would like to own a {my_own_list[-2].upper()} car!"
print(car_0)
print(car_1)
print(car_2)
print(car_3)
