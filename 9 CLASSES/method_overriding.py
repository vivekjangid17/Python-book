class Animal:
    
    def speak(self):
        return "Some generic sound"
    
class Dog(Animal):
    
    def speak(self):
        return "Bark"

animal = Animal()
print(animal.speak())

dog = Dog()
print(dog.speak())