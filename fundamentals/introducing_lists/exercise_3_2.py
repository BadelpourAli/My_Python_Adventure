# 3-4. Guest List: 
# If you could invite anyone, living or deceased, to dinner, who would you invite? 
# Make a list that includes at least three people you’d like to invite to dinner. 
# Then use your list to print a message to each person, inviting them to dinner.

dinner_party = []
dinner_party.append('sara')
dinner_party.insert(1, 'david')
dinner_party.insert(2, 'jack')
print(f"Hey {dinner_party[0].title()}! You are invited to the Party!")
print(f"Hey {dinner_party[1].title()}! You are invited to the Party!")
print(f"Hey {dinner_party[2].title()}! You are invited to the Party!")

# 3-5. Changing Guest List:
# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
# You’ll have to think of someone else to invite.
# • Start with your program from Exercise 3-4. 
# Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in your list.

dinner_party_modified_1 = ['sara', 'david', 'jack']
print(f"I can't come! - {dinner_party_modified_1[1].upper()}")
dinner_party_modified_1[1] = 'sam'
print(f"I'll come instead of David! - {dinner_party_modified_1[1].upper()}")
print(f"I'll come! - {dinner_party_modified_1[0].upper()}")
print(f"I'll come! - {dinner_party_modified_1[1].upper()}")
print(f"I'll come! - {dinner_party_modified_1[-1].upper()}")

# 3-6. More Guests: 
# You just found a bigger dinner table, so now more space is available.
# Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5.
# Add a print() call to the end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

dinner_party_modified_2 = ['sara', 'sam', 'jack']
print("We just found a bigger dinner table!!!")
dinner_party_modified_2.insert(3, 'rebeeca')
dinner_party_modified_2.insert(4, 'tony')
dinner_party_modified_2.append('emilia')
print(f"A bigger dinner table! \tYou are invited {dinner_party_modified_2[0].title()}!")
print(f"A bigger dinner table! \tYou are invited {dinner_party_modified_2[1].title()}!")
print(f"A bigger dinner table! \tYou are invited {dinner_party_modified_2[2].title()}!")
print(f"A bigger dinner table! \tYou are invited {dinner_party_modified_2[3].title()}!")
print(f"A bigger dinner table! \tYou are invited {dinner_party_modified_2[4].title()}!")
print(f"A bigger dinner table! \tYou are invited {dinner_party_modified_2[5].title()}!")

# 3-7. Shrinking Guest List: 
# You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# • Start with your program from Exercise 3-6. 
# Add a new line that prints a message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. 
# Each time you pop a name from your list, 
# print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty list. 
# Print your list to make sure you actually have an empty list at the end of  your program.

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
del dinner_party_modified_3[0]
del dinner_party_modified_3[0]
print(dinner_party_modified_3)
