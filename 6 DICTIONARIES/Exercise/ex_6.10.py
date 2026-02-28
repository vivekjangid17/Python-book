'''6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so each person can have more than one favorite number. Then print each person's name along with their favorite numbers.'''

fav_number = {'kanak': [5,45,76,87], 
    'riya': [7,67,95,56],
    'rohit': [45,70,26,43],
    'virat': [18,75,8,9],
    'vivek': [17,4,1,18],
}

for key, value in fav_number.items():
    print(f"{key.title()}'s favorite numbers are: ")
    for number in value:
        print(number,end=",")
    print("\n")
