# 8-6. City Names:
# Write a function called city_country() that takes in the name of a city and its country. 
# The function should return a string formatted like this: "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city, country):
    pair = f"\n{city}, {country}"
    return pair.title()
paired = city_country("london", "UK")
print(paired)
paired = city_country("berlin", "germany")
print(paired)
paired = city_country("osaka", "japan")
print(paired)

# 8-7. Album:
# Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
# Use the function to make three dictionaries representing different albums. 
# Print each return value to show that the dictionaries are storing the album information correctly.
# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
# If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
# Make at least one new function call that includes the number of songs on an album.

def make_album(artist_name, album_title):
    dict_album = {"Artist": {artist_name.title()}, "Album": {album_title.title()}}
    return dict_album
album_1 = make_album("eminem", "the marshall mathers LP 2")
print(album_1)
album_2 = make_album("pink floyd", "this is pink floyd")
print(album_2)
album_3 = make_album("imagine dragons", "mercury i")
print(album_3)

# Making space
print()

def make_album(artist_name, album_title, number_of_song=None):
    if number_of_song:
        dict_album = {"Artist": artist_name.title(), "Album": album_title.title(), "Number": number_of_song}
    else:
        dict_album = {"Artist": artist_name.title(), "Album": album_title.title()}
    return dict_album
album_1 = make_album("eminem", "the marshall mathers LP 2")
print(album_1)
album_2 = make_album("pink floyd", "this is pink floyd")
print(album_2)
album_3 = make_album("imagine dragons", "mercury i", 8)
print(album_3)

# 8-8. User Album:
# Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. 
# Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
# Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title, number_of_songs=None):
    album_dict = {"Artist": artist_name.title(), "Album": album_title.title()}
    if number_of_songs:
        album_dict["Number of Songs"] = number_of_songs
    return album_dict

print(f"\nWelcome to the album dictionary maker!")
while True:
    print("(enter 'q' at any time to quit)")
    a_name = input("Artist name: ")
    if a_name.lower() == 'q':
        break
    al_name = input("Album name: ")
    if al_name.lower() == 'q':
        break
    detailed_album = make_album(a_name, al_name)
    print(detailed_album)