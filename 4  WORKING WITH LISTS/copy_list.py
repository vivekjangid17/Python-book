my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# my_foods.append('rasogulla')
# print(my_foods)
# print(friend_foods)

# This doesn't work:
friend_foods = my_foods
my_foods.append('momos')
friend_foods.append('paw bhaji')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# Python List Assignment is by Reference (Not Copy)
# In Python, variables that hold lists don’t store the list itself, but a reference (or pointer) to the memory location where the list is stored.

# When you assign a list to another variable, you are not creating a new list; instead, you are creating a new reference to the same list in memory.
# my_foods = ['pizza', 'falafel', 'carrot cake']
# At this point:

# my_foods holds a reference to the actual list ['pizza', 'falafel', 'carrot cake']