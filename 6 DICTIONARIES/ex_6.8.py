'''6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner's name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.'''

pet1 = {'kind': 'dog', 'owner': 'Alice'}
pet2 = {'kind': 'cat', 'owner': 'Bob'}
pet3 = {'kind': 'parrot', 'owner': 'Charlie'}
pet4 = {'kind': 'rabbit', 'owner': 'Diana'}
pet5 = {'kind': 'hamster', 'owner': 'Ethan'}
pet6 = {'kind': 'goldfish', 'owner': 'Fiona'}
pet7 = {'kind': 'turtle', 'owner': 'George'}
pet8 = {'kind': 'lizard', 'owner': 'Hannah'}
pets = [pet1, pet2, pet3, pet4, pet5, pet6, pet7, pet8]
for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print()   # for space between each combination