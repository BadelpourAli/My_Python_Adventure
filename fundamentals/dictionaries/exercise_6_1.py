# 6-1. Person: 
# Use a dictionary to store information about a person you know. 
# Store their first name, last name, age, and the city in which they live. 
# You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

my_friend = {'first_name': 'john', 'last_name': 'smith', 'age': 25, 'city': 'new york'}
print(my_friend['first_name'].title())
print(my_friend['last_name'].title())
print(my_friend['age'])
print(my_friend['city'].title())

# 6-2. Favorite Numbers: 
# Use a dictionary to store people’s favorite numbers. 
# Think of five names, and use them as keys in your dictionary. 
# Think of a favorite number for each person, and store each as a value in your dictionary. 
# Print each person’s name and their favorite number.
# For even more fun, poll a few friends and get some actual data for your program.

favorite_numbers = {'john': 5, 'sara': 1, 'emilia': 7, 'sam': 18, 'tony': 6}
print("\nFavorite Numbers: ")
print(f"John: {favorite_numbers['john']}")
print(f"Sara: {favorite_numbers['sara']}")
print(f"Emilia: {favorite_numbers['emilia']}")
print(f"Sam: {favorite_numbers['sam']}")
print(f"Tony: {favorite_numbers['tony']}")

# 6-3. Glossary: 
# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output. 
# You might print the word followed by a colon and then its meaning, 
# or print the word on one line and then print its meaning indented on a second line. 
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {'variable': 'A container for a value (string, integer, float, boolean).',
            'conditional expression': 'A one-line shortcut for the if-else statement (ternary operator).',
            'indexing': 'Accessing elements of a sequence using [] (indexing operator).',
            'format specifiers': 'Format a value based on what flags are inserted {value:flags}.',
            'logical operators': 'Evaluate multiple conditions (or, and, not).' 
            }
print("\nHere's my personal glossary about My_Python_Adventure!")
print(f"variable:\n\t{glossary['variable']}")
print(f"conditional expression:\n\t{glossary['conditional expression']}")
print(f"indexing:\n\t{glossary['indexing']}")
print(f"format specifiers:\n\t{glossary['format specifiers']}")
print(f"logical operators:\n\t{glossary['logical operators']}")
