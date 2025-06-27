# Removing All Instances of Specific Values from a List

# for loop
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
for pet in pets[:]:
    if pet == 'cat':
        pets.remove(pet)

print(pets)

# while loop
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
    pets.remove('cat')

print(pets)

    
