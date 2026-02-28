'''7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you'll add that topping to their pizza.'''

# prompt = "Please enter pizza toppings.\nEnter 'quit' when you finished: "
# tp = []

# while True:
#     topping = input(prompt)
#     if topping == 'quit':
#         break 
#     print(topping)
#     if topping not in tp:
#         tp.append(topping)

# print(f"You have enterd the list of toppings: {tp}")


prompt = "Please enter pizza toppings.\nEnter 'quit' when you're finished: "
tp = []

while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    print(f"Okay! We'll add {topping} to your pizza.")
    if topping.lower() not in tp:  # prevent case-sensitive duplicates
        tp.append(topping)

if tp:
    print("\nYou have entered the following toppings for your pizza:")
    for t in tp:
        print(f"- {t.capitalize()}")
else:
    print("You didn't add any toppings to your pizza.")
