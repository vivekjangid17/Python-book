# How the input() Function Works
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name: "
name = input(prompt)
print(f"Hello, {name}")

# Using int() to Accept Numerical Input
# Python interprets everything the user enters as a string
age = input("Enter your age: ")
print(age)
print(type(age))     # <class 'str'>

# use int()
age = int(input("Enter age: "))
print(age)
print(type(age))     # <class 'int'>

# The Modulo Operator : returns the remainder
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = a % b
print(c)
