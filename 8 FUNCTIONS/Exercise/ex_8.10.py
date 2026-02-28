''' 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it's printed. After calling the function, print both of your lists to make sure the messages were moved correctly.'''

messages = ["Hii", "Hello", "How are you ?", "I am good."]
sent_messages = []


def send_messages(messages):
    # for message in messages:
        # print(message)
    while messages:
        current_message = messages.pop()
        print(f"The current message is {current_message}")
        sent_messages.append(current_message)
        
send_messages(messages)

print(messages)
print(sent_messages)
