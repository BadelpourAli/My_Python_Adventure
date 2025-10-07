# 8-12. Sandwiches: 
# Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as manyitems as the function call provides, 
# and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.

def sandwich_order(*args):
    for arg in args:
        print(f"The {arg} is added to your sandwich!")
    print(" ")
sandwich_order("ketchup sauce", "salt cucumber")
sandwich_order("tomato")
sandwich_order("ketchup sauce", "salt cucumber","lettuce")

# 8-13. User Profile:
# Start with a copy of user_profile.py. 
# Build aprofile of yourself by calling build_profile(), 
# using your first and last names and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info
user_profile = build_profile(
    'sam', 'wood',
    location='Tokyo',
    field='Cyber Security')
print(user_profile)

# 8-14. Cars:
# Write a function that stores information about a car in a dictionary. 
# The function should always receive a manufacturer and a model name. Itshould then accept an arbitrary number of keyword arguments. 
# Call the function with the required information and two other name-value pairs, such as acolor or an optional feature. 
# Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was stored correctly.

def make_car(manufacturer, model_name, **kwargs):
    """Store information about a car in a dictionary."""
    car_info = {
        'manufacturer': manufacturer.title(),
        'model': model_name.title()
    }
    car_info.update(kwargs)
    return car_info

user_1 = make_car(
    "lambo",
    "aventador",
    color='blue',
    price='1M pounds'
)
print(user_1)

user_2 = make_car('ferrari', 'sf90', color='red', price='1M pounds')
print(user_2)