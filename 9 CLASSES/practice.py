# I am creating a class Area that calculates area of rectangle

class Area:
    length = 2
    width = 3
    # without init() method length and width are same for all the objects, but if we want to create different objects then we can use init() method.
    
    def area(self):
        print(self.length*self.width)
    
a = Area()
a.area()

        
    
    