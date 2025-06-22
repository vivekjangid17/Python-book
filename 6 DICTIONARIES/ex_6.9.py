'''6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person's name and their favorite places.'''

favorite_places = {
    'kanak': ['jaipur', 'manali', 'paris'],
    'devid': ['paris', 'manali', 'udaipur'],
    'virat': ['new york', 'rishikesh', 'sikkim'],
}
print(favorite_places)  # print the whole dict

for i,j in favorite_places.items():
    print(f"{i.title()}'s favorite places are: ")
    for k in j:
        print(k.title())
    print("")