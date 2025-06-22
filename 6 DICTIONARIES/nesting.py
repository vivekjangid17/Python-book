# A List of Dictionaries

dict1 = {'color': 'green', 'points': 5}
dict2 = {'color': 'yellow', 'points': 10}
dict3 = {'color': 'red', 'points': 15}

list = [dict1, dict2, dict3]
for i in list:
    print(i)

print()

# Make an empty list for storing aliens.
aliens = []
# new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}

# IMPORTANT NOTE:
# In this version, we are appending the same dictionary (new_alien) 30 times to the list.
# This means all 30 elements in the list refer to the SAME alien object in memory.
# So, if we change one alien, all of them will change — because they are just different references to the same object.

# To create 30 separate aliens (independent objects), we must define the dictionary INSIDE the loop like this:

for i in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# change the first three aliens to yellow, medium-speed aliens worth 10 points each
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# A List in a Dictionary

student = {
    'class': 12,
    'subjects': ['english', 'maths', 'hindi'],
}
# loop through the list of values of the key subjects
for subject in student['subjects']:
    print(subject)
print(type(student['subjects']))