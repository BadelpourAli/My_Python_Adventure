# 6-4. Glossary 2:
# Now that you know how to loop through a dictionary, 
# clean up the code from Exercise 6-3 by 
# replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. 
# When you’re sure that your loop works, add five more Python terms to your glossary. 
# When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {'variable': 'A container for a value (string, integer, float, boolean).',
            'conditional expression': 'A one-line shortcut for the if-else statement (ternary operator).',
            'indexing': 'Accessing elements of a sequence using [] (indexing operator).',
            'format specifiers': 'Format a value based on what flags are inserted {value:flags}.',
            'logical operators': 'Evaluate multiple conditions (or, and, not).' 
            }
print("\nHere's my personal glossary about My_Python_Adventure!")
for term, definition in glossary.items():
    print(f"\nTerm: {term}")
    print(f"\n\tDefinition: {definition}")

glossary['f(format) string'] = 'print(f”your text + {variable}”).'
glossary['Typecasting'] = 'the process of converting a variable from one data type to another.'
glossary['if conditionals'] = 'do some code only if some condition is True, else do something else.'
glossary['for loops'] = 'execute a block of code a fixed number of times. You can iterate over a range, string, sequence, etc.'
glossary['nested loops'] = 'a loop within another loop (outer, inner).'

print("\nRunning the program for the second time: ")
print("\nHere's my personal glossary about My_Python_Adventure!")
for term, definition in glossary.items():
    print(f"\nTerm: {term}")
    print(f"\n\tDefinition: {definition}")

# 6-5. Rivers:
# Make a dictionary containing three major rivers and the country each river runs through. 
# One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers = {'nile': 'egypt', 'amazon': 'brazil', 'mississippi': 'united states'}

print("Rivers and their countries:")
for river, country in rivers.items():
    print(f"\nThe {river.title()} runs through {country.title()}.")

print("\nThe rivers are:")
for river in rivers.keys():
     print(river.title())

print("\nThe countries are:")
for country in rivers.values():
    print(country.title())

# 6-6. Polling: 
# Use the code in favorite_languages.py
# • Make a list of people who should take the favorite languages poll.
# Include some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. 
# If they have already taken the poll, print a message thanking them for responding. 
# If they have not yet taken the poll, print a message inviting them to take the poll.

people_to_poll = ['jen', 'sarah', 'edward', 'phil', 'tom', 'emilia', 'tony']

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

print("\nWelcome to the favorite programming language poll: (MK II) ")
for person in people_to_poll:
    if person in favorite_languages:
         print(f"\nThank you, {person.title()}, for taking the poll!")
    else: 
         print(f"\n{person.title()}, pelase tak our poll!")
