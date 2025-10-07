# 8-3. T-shirt:
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments.

def make_shirt(size, message):
    print(f"\nThe size of the shirt is: \n{size}.")
    print(f"The message on the shirt is: \n{message}.")
make_shirt("XL", "Let's heal the world")
make_shirt(message= "Let the darkness lead us into the light...", size= "S")

# 8-4. Large Shirts:
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, 
# and a shirt of any size with a different message.

def make_shirt(size= "Large", message= "I love Python"):
    print(f"\nMy shirt is {size}. And it has this sentence on it: {message}.")
make_shirt()
make_shirt(size= "Medium")
make_shirt(size= "Small", message= "I love C#")

# 8-5. Cities:
# Write a function called describe_city() that accepts the name of a city and its country. 
# The function should print a simple sentence, such as Reykjavik is in Iceland. 
# Give the parameter for the country a default value. 
# Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city, country= "U.S"):
    print(f"\nThe {city.title()} is in {country}.")
describe_city("new york")
describe_city("tokyo", country= "Japan")
describe_city("london")