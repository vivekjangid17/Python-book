'''6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.'''

fav_number = {'kanak': 5, 'riya': 7, 'rohit': 45, 'virat': 18, 'vivek': 17}
print(fav_number.items())
for i, j in fav_number.items():  # the method items(), returns a sequence of key-value pairs
    print(f'{i}: {j}')
