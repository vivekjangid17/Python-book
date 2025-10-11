'''8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.'''


def show_messages(messages):
    for message in messages:
        print(message)
        
messages = ["Hii", "Hello", "How are you ?", "I am good."]

show_messages(messages)