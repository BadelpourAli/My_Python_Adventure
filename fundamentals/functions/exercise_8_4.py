# 8-9. Messages: 
# Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message.

messages = [
    "I love Python.",
    "I hate Java",
    "I am ok with C#."
]
def show_messages():
    for item in messages:
        print(item)

show_messages()

# 8-10. Sending Messages:
# Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and 
# moves each message to a new list called sent_messages as it’s printed. 
# Aftercalling the function, print both of your lists to make sure the messages weremoved correctly.

messages = [
    "I love Python.",
    "I hate Java",
    "I am ok with C#."
]

sent_messages = []

def send_messages(message_list, sent_list):
    while message_list:
        current_message = message_list.pop(0)
        print(f"Sending: {current_message}")
        sent_list.append(current_message)

send_messages(messages, sent_messages)
print(f"\nOriginal messages: {messages}")
print(f"Sent messages: {sent_messages}")

# 8-11. Archived Messages:
# Start with your work from Exercise 8-10. 
# Call the function send_messages() with a copy of the list of messages. 
# After calling the function, print both of your lists to show that the original list has retained its messages.

messages = [
    "I love Python.",
    "I hate Java",
    "I am ok with C#."
]

sent_messages = []

def send_messages(message_list, sent_list):
    while message_list:
        current_message = message_list.pop(0)
        print(f"Sending: {current_message}")
        sent_list.append(current_message)

send_messages(messages[:], sent_messages) 
print(f"\nOriginal messages: {messages}")
print(f"Sent messages: {sent_messages}")