'''9-4. Number Served: Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again.Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who've been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business'''


class Restaurant:
    
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        # self.number_served = 5
    
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The cuisine type in this restaurant is {self.cuisine_type}.")
        print(f"{self.number_served} customers have served by this restaurant")
        print()
        
    def set_number_served(self,customer):
        self.number_served = customer
        
    def increment_number_served(self,customer):
        self.number_served += customer
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for 24/7 days.")
    
    
restaurant = Restaurant('Pavitra Bhojnalaya', 'Pure Vegetarian')
restaurant.describe_restaurant()
restaurant.set_number_served(5)
restaurant.describe_restaurant()
restaurant.increment_number_served(100)
restaurant.describe_restaurant()

