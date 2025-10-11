'''8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.'''

messages = ["Hii", "Hello", "How are you ?", "I am good."]
sent_messages = []


def send_messages(messages):
    # for message in messages:
        # print(message)
    while messages:
        current_message = messages.pop()
        print(f"The current message is {current_message}")
        sent_messages.append(current_message)
        
send_messages(messages[:])

print(messages)
print(sent_messages)