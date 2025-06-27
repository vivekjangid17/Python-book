# Using break to Exit a Loop

# Consider a program that asks the user about places they've visited. We can stop the while loop in this program by calling break as soon as the user enters the 'quit' value:
prompt = "Enter the name of city you like to visit.\n(Enter 'quit' when you are finished): "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    print(f"I would love to visit {city.title()}.")

# Using continue in a Loop

# Consider a loop that counts from 1 to 10 but prints only the odd numbers in that range:
i = 0
while i<10:
    i+=1
    if i % 2 == 0:
        continue
    print(i)
