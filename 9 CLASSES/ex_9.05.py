'''9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.'''

class User:
    
    def __init__(self, first_name, last_name, age, email, city, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city
        self.login_attempts = login_attempts
        
    def describe_user(self):
        print("User Information:")
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("City:", self.city)
        print("Login_attempts:", self.login_attempts)
        print("----------------------")
        
    # Method to greet user
    def greet_user(self):
        print("Hello", self.first_name + "!", "Welcome back 😊")
        print()
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'Login attempts after increment: {self.login_attempts}')
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'Login attempts after reset: {self.login_attempts}')
        
# Creating different user objects

user1 = User("Vivek", "Jangid", 21, "vivek@gmail.com", "Alwar",2)

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()

