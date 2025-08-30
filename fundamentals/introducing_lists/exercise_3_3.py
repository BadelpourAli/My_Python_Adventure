# 3-8. Seeing The World: 
# Think of at least five places in the world you’d like to visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that its order has changed.
# • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.

favorite_places = ['Tokyo', 'New York','Paris', 'Amsterdam', 'Berlin']
print("\nThe list is in original order:")
print(favorite_places)
print("\nThe list is in alphabetic order Temporarily:")
print(sorted(favorite_places))
print("\nThe list is still in original order:")
print(favorite_places)
print("\nThe list is now in reverse-alphabetical order Temporarily:")
print(sorted(favorite_places, reverse=True))
print("\nThe list is still in original order:")
print(favorite_places)
favorite_places.reverse()
print("\nThe list is now reversed Permanently:")
print(favorite_places)
favorite_places.reverse()
print("\nThe list is now in original form again Permanently:")
print(favorite_places)
favorite_places.sort()
print("\nThe list is in alphabetical order Permanently:")
print(favorite_places)
favorite_places.sort(reverse = True)
print("\nThe list is now in reverse-alphabetical order Permanently:")
print(favorite_places)

# 3-9. Dinner Guests: 
# Working with one of the programs from Exercises 3-4 through 3-7, 
# use len() to print a message indicating the number of people you’re inviting to dinner.

dinner_party_modified_3 = ['sara', 'sam', 'jack', 'rebeeca', 'tony', 'emilia']
print("Guys! \tOur new dinner table won't arrive in time! \nSorry, but I can invite only TWO guests!")
first_removal = dinner_party_modified_3.pop(0)
print(f"Sorry, {first_removal.title()}, but we won't be able to include you this time.")
second_removal = dinner_party_modified_3.pop(-1)
print(f"Sorry, {second_removal.title()}, but we won't be able to include you this time.")
third_removal = dinner_party_modified_3.pop(0)
print(f"Sorry, {third_removal.title()}, but we won't be able to include you this time.")
fourth_removal = dinner_party_modified_3.pop(1)
print(f"Sorry, {fourth_removal.title()}, but we won't be able to include you this time.")
print(f"{dinner_party_modified_3[0].title()}, you are still invited!")
print(f"{dinner_party_modified_3[1].title()}, you are still invited!")
number_of_invited_people = len(dinner_party_modified_3)
print(f"\nThe number of invited people: {number_of_invited_people}")

# 3-10. Every Function: 
# Think of things you could store in a list. 
# For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

languages = ['Spanish', 'English', 'Japanese',]
print(languages)
print(languages[0])
print(languages[-1].upper())
message = f"My favorite language is {languages[1]}!"
print(message)
languages[2] = 'French'
print(languages)
languages.append('Italian')
print(languages)
languages.insert(0, 'Russian')
print(languages)
del languages[3]
print(languages)
popped_language = languages.pop()
print(popped_language)
last_learned_language = languages.pop()
print(f"The last language that I learned was the {last_learned_language}.")
first_learned_language = languages.pop(0)
print(f"The {first_learned_language} was the first language I learned.")
languages.remove('Spanish')
print(languages)
languages.append('Russian')
languages.append('English')
languages.append('Persian')
print(languages)
hard_language = 'Russian'
languages.remove(hard_language)
print(languages)
print(f"\nThe {hard_language.upper()} language is too hard to learn.")
print(sorted(languages))
print(sorted(languages, reverse=True))
languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)
languages.reverse()
print(languages)
print(len(languages))
