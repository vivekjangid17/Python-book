'''9-3. Users: Make a class called User. Create two attributes called first_name  and last_name, and then create several other attributes that are typically stored  in a user profile. Make a method called describe_user() that prints a summary  of the user's information. Make another method called greet_user() that prints  a personalized greeting to the user. Create several instances representing different users, and call both methods for each user'''


class User:
    
    def __init__(self, first_name, last_name, age, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city
        
    def describe_user(self):
        print("User Information:")
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("City:", self.city)
        print("----------------------")
        
    # Method to greet user
    def greet_user(self):
        print("Hello", self.first_name + "!", "Welcome back 😊")
        print()
        
# Creating different user objects

user1 = User("Vivek", "Jangid", 21, "vivek@gmail.com", "Alwar")
user2 = User("Rohit", "Sharma", 20, "rohit@gmail.com", "Jaipur")
user3 = User("Rahul", "Verma", 22, "rahul@gmail.com", "Delhi")

# Calling methods for each user

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
        
