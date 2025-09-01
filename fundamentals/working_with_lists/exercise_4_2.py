# 4-3. Counting to Twenty: 
# Use a for loop to print the numbers from 1 to 20, inclusive.

for number in range(1, 21):
    print(number)

# 4-4. One Milion: 
# Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
# (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

numbers = []
for number in range(1, 1000001):
    numbers.append(number)    
print(numbers)

# 4-5. Summing a Milion: 
# Make a list of the numbers from one to one million, 
# and then use min() and max() to make sure your list actually starts at one and ends at one million. 
# Also, use the sum() function to see how quickly Python can add a million numbers.

million_numbers = list(range(1, 1000001))
print(million_numbers)
print(f"This is the minimum number of our list: {min(million_numbers)}")
print(f"This is the maximum number of our list: {max(million_numbers)}")
print(f"This is the sum of this list of numbers: {sum(million_numbers)}")

# 4-6. Odd numbers:
# Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
# Use a for loop to print each number. 

odd_numbers = []
for number in range(1, 21, 2):
    odd_numbers.append(number)
print(f"\nThis is the odd numbers from 1 to 20: {odd_numbers}")

# 4-7. Threes:
# Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

threes = []
for number in range(3, 31):
    threes.append(number ** 3)
print(f"\nThis is the list of multiples of 3 from 3 to 30: {threes}")

# 4-8. Cubes:
# A number raised to the third power is called a cube. 
# For example, the cube of 2 is written as 2**3 in Python.
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
# and use a for loop to print out the value of each cube.

cubes = []
for number in range(1, 11):
    cubes.append(number ** 3)
print(f"\nThis is the list of cubes numbers from 1 to 10: {cubes}")

# 4-9. Cube Comprehension:
# Use a list comprehension to generate a list of the first 10 cubes.

cube_comprehension = [number ** 3 for number in range(1, 11)]
print(f"\nThis is the list comprehension of generating a list of the first 10 cubes: {cube_comprehension}")
