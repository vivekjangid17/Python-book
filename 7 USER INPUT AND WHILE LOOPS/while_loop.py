# The for loop takes a collection of items and executes a block of code once for each item in the collection

# The while loop runs as long as, or while, a certain condition is true.
# while loop counts from 1 to 5:
i = 1
while (i<=5):
    print(i)
    i+=1

# Letting the User Choose When to Quit
prompt = "Enter 'quit' to end the program: "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# Using a Flag
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)