'''9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.'''
# importing the class Restaurant from exercise 9.01

from restaurant import Restaurant

class IceCreamStand(Restaurant):
    
    def __init__(self,restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.icecream_flavors = ["Vanilla", "Chocolate", "Strawberry", "Mango", "Butterscotch"]
        
    def display_flavors(self):
        print("Icecream flavors are...")
        for icecream in self.icecream_flavors:
            print(icecream)
            
icecream = IceCreamStand('Pavitra Bhojnalaya', ' Pure Vegetarian')
icecream.display_flavors()