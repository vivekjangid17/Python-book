# A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. A key's value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary. In Python, a dictionary is wrapped in braces ({}) with a series of key-value pairs inside the braces.

student = {'name': 'chris', 'class': '6', 'section': 'A'}
print(student['name'])
print(student['section'])
print(student)

# Adding New Key-Value Pairs
student['age'] = 12
student['marks'] = 85
print(student)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    alien_0['x_position'] = alien_0['x_position'] + 1
elif alien_0['speed'] == 'medium':
    alien_0['x_position'] = alien_0['x_position'] + 2
else:
    # This must be a fast alien.
    alien_0['x_position'] = alien_0['x_position'] + 3

print(f"New position: {alien_0['x_position']}")

# Removing Key-Value Pairs
del student['marks']
print(student
      )  # Be aware that the deleted key-value pair is removed permanently.

###### Using get() to Access Values  #####

# when we use square brackets to retrive the value of a key and if the key doesn't exits, we will get an error. To avoid this error we use get() method to acces the value.

s_marks = student.get(
    'marks', 'No marks assigned.'
)  # The get() method requires a key as a first argument. As a second optional argument, you can pass the value to be returned if the key doesn’t exist
print(s_marks)
