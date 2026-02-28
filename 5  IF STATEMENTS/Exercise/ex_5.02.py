# Tests for equality and inequality with strings
name = "Krishana"
print(name == "Krishana") # True
print(name != "Krishana") # False

# Tests using the lower() method
print(name.lower() == "krishana") # True
print(name.lower() != "krishana") # False

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
age = 19
print(age == 19) # True
print(age != 19) # False
print(age >= 18 & age <= 20) # True

# Tests using the and keyword and the or keyword
print((age > 18) and (age < 20)) # True
print((age > 18) or (age < 19)) # True

# Test whether an item is in a list
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits) # True
print("grape" in fruits) # False