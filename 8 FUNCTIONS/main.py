# Defining a Function

def greet():
    print('Hello Vivek, Good Morning.')


for i in range(1,6):
    greet()

# Passing Information to a Function

def greet_user(user):
    print(f"Hello, {user.title()}")


user = input("Enter name: ")
greet_user(user)