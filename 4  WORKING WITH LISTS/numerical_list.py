# Using the range() Function
for i in range(1,6):
    print(i, end=' ')
print()   
# Using range() to Make a List of Numbers
numbers = list(range(1,6))
print(numbers)

# Using range() to Make a List of Even Numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Square of numbers
square = []
for i in range(1,11):
    square.append(i**2)
print(square)

# Simple Statistics with a List of Numbers
numbers = [1, 2, 3, 4, 5]
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))
