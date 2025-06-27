'''7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.'''

prompt = "Please enter pizza toppings.\nEnter 'quit' when you're finished: "

# 1

topping1 = ""
while topping1.lower() != 'quit':
    topping1 = input(prompt)
    if topping1.lower() != 'quit':
        print(topping1)

# 2

active = True
while active:
    topping2 = input(prompt)
    if topping2.lower() != 'quit':
        print(topping2)
    else:
        active = False

# 3

while True:
    topping3 = input(prompt)
    if topping3 == 'quit':
        break
    print(topping3)