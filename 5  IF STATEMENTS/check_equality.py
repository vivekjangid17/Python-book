car = 'bmw'
print(car == 'bmw')   # True

# Using or to Check Multiple Conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)   # True
print(age_0 >= 21 and age_1 >= 21)   # False
print(age_0 >= 21 and age_1 >= 18)   # True

# Checking Whether a Value Is in a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('bmw' in cars)   # True
print('audi' in cars)   # True
print('Thar' in cars)   # False
print('Thar' not in cars)   # True