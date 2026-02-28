'''9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.'''

# we can also import the same file inside this python file but due to name of the file we are avoiding this right now, we will do it later



class Restaurant:
    
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The cuisine type in this restaurant is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for 24/7 days.")
    
    
restaurant1 = Restaurant('Pavitra Bhojnalaya', "Pure Vegetarian")
restaurant1.describe_restaurant()
restaurant2 = Restaurant("Punjabi Dhaba", "Pure Punjabi")
restaurant2.describe_restaurant()
restaurant3 = Restaurant("Rajasthani Dhaba", "Pure Rajasthani")
restaurant3.describe_restaurant()
