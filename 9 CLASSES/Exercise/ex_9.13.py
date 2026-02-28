'''9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.'''

import random

class Die:
    
    def __init__(self):
        self.side1 = 6
        self.side2 = 10
        self.side3 = 20
        
    def roll_die(self):
        if self.side1:
            for i in range(1,11):
                print(f'Random number between 1 and {self.side1} is {random.randint(1,self.side1)}')
        if self.side2:
            for j in range(1,11):
                print(f'Random number between 1 and {self.side2} is {random.randint(1,self.side2)}')
        if self.side3:
            for k in range(1,11):
                print(f'Random number between 1 and {self.side3} is {random.randint(1,self.side3)}')
        
d = Die()
d.roll_die()
        