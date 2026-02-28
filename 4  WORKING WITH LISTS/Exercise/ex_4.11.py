''' My_fruits, Your_fruits: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of_fruits, and call it friend_fruits. Then, do the 
following: '''

fruits = ["apple", "banana", "orange","mango"]
friend_fruits = fruits[:]

# Add a new pizza to the original list.
fruits.append("papaya")
# Add a different pizza to the list friend_fruits.
friend_fruits.append("pomegrenate")

print("My favorite fruits are:")
for fruit in fruits:
    print(fruit)
    
print("\nMy friend's favorite fruits are:")
for f_fruit in friend_fruits:
    print(f_fruit)