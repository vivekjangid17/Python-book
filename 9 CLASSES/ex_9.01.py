'''9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.'''

class Restaurant:
    
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The cuisine type in this restaurant is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for 24/7 days.")
    
    
restaurant = Restaurant('Pavitra Bhojnalaya', ' Pure Vegetarian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
