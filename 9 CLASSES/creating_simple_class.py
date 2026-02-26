# Creating the Dog Class

class Dog:
    # without __init__() method ke name & age will be same for all objects
    # if we wants the different value for different objects then we have to use __init__().
    # name = 'Kalu'
    # age = '3'
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self,place):
        print("Good morning,",self.name, place, "pe ja rhe ho...")
    
obj = Dog("kalu",4)
print(obj.name)
obj2 = Dog(name="Bhura",age=3)
print(obj2.name)
# print(obj.greet())   # requires self as a parameter
obj.greet('thikane')
        