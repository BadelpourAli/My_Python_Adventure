# 6-7. People:
# Start with the program you wrote for Exercise 6-1.
# Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
# Loop through your list of people. As you loop through the list, print everything you know about each person.

people = [
    {'first_name': 'john', 'last_name': 'smith', 'age': 25, 'city': 'new york'},
    {'first_name': 'sam', 'last_name': 'williams', 'age': 17, 'city': 'tokyo'},
    {'first_name': 'edward', 'last_name': 'stones', 'age': 48, 'city': 'london'}
]
print("People Information:")
for person in people:
    print(f"\nName: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")

    
# 6-8. Pets: 
# Make several dictionaries, where each dictionary represents a different pet.
# In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. 
# Next, loop through your list and as you do, print everything you know about each pet.

pets = [
    {'owner': 'emilia', 'animal': 'cat'},
    {'owner': 'john', 'animal': 'dog'},
    {'owner': 'sara', 'animal': 'hamster'},
    {'owner': 'jack', 'animal': 'rabbit'},
    {'owner': 'rebecca', 'animal': 'fish'}
]
print("\nPet Information:")
for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['animal']}.")
    
# 6-9. Favorite Places: 
# Make a dictionary called favorite_places. 
# Think of three names to use as keys in the dictionary, 
# and store one to three favorite places for each person. 
# To make this exercise a bit more interesting, 
# ask some friends to name a few of their favorite places. 
# Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places = {
    'sam': ['new york', 'london', 'berlin'],
    'sara': ['amsterdam'],
    'tom': ['tokyo', 'kyoto'],
    }
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite place(s) is/are:")
    for place in places:
        print(f"\n{place.title()}")

# 6-10. Favorite Numbers: 
# Modify your program from Exercise 6-2 so each person can have more than one favorite number.
# Then print each person’s name along with their favorite numbers.

favorite_numbers = {
    'john': [1],
    'sara': [1, 7],
    'emilia': [9, 17, 100],
    'sam': [22, 55, 77],
    'tony': [None]
    }
print("\nFavorite Numbers:")
for name, numbers in favorite_numbers.items():
    print(f"\nFavorite number(s) of {name.title()}:")
    for number in numbers:
        print(number)
        
# 6-11. Cities:
# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country that the city is in, 
# its approximate population, and one fact about that city.
# The keys for each city’s dictionary should be something like country, population, and fact. 
# Print the name of each city and all of the information you have stored about it.

cities = {
    'new york': {
        'location': 'usa',
        'population': '8.4M',
        'fact': 'New York City is the most populous city in the U.S.',
     },
    'tokyo': {
        'location': 'japan',
        'population': '37M',
        'fact': 'The world’s oldest company is in Tokyo. (Kongō Gumi)',
    },
    'amsterdam': {
        'location': 'Netherlands',
        'population': '1M',
        'fact': 'There are 1.2 million bikes in this city.',
    },
}
print("\nCity Information:")
for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Location: {city_info['location'].upper()}")
    print(f"Population: {city_info['population']}")
    print(f"Fact: {city_info['fact']}")
    
# 6-12. Extensions: 
# We’re now working with examples that are complex enough that they can be extended in any number of ways.
# Use one of the example programs from this chapter, 
# and extend it by adding new keys and values, changing the context of the program, 
# or improving the formatting of the output.

print(f"\n The Extension:")
cities = {
    'new york': {
        'location': 'usa',
        'population': '8.4 M',
        'fact': 'New York City is the most populous city in the U.S.',
    },
    'tokyo': {
        'location': 'japan',
        'population': '37 M',
        'fact': 'The world’s oldest company is in Tokyo. (Kongō Gumi)',
    },
    'amsterdam': {
        'location': 'Netherlands',
        'population': '1 M',
        'fact': 'There are 1.2 million bikes in this city.',
    },
}
print("\nThe list of cities: ")

for city in cities:
    print(city.title())
missed_city = cities.get('Berlin', 'N/A')
print(f"\nMissed city: Berlin {missed_city}")

cities['berlin'] = {
    'location': 'germany',
    'population': '4.6 M',
    'fact': 'Berlin is the greenest city in Europe.',
}

print("The city 'Berlin' is added.")
print("\nThe list of cities: ")
for city in cities:
    print(city.title())
    
for city, city_info in sorted(cities.items()):
    print(f"\nCity: {city.title()}")
    print(f"Location: {city_info['location'].upper()}")
    print(f"Population: {city_info['population']}")
    print(f"Fact: {city_info['fact']}")
