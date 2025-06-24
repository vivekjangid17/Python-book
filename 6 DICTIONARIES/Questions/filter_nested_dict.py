'''4. Filter Nested Dictionaries by Condition
Given a nested dictionary, return a new dictionary with only those inner dictionaries where a specific condition is true.'''

students = {
    101: {"name": "Amit", "marks": 88},
    102: {"name": "Riya", "marks": 92},
    103: {"name": "Sohan", "marks": 67}
}

# Filter students with marks >= 90
# Output: {102: {'name': 'Riya', 'marks': 92}}

f = {}
for s_id, s_info in students.items():
    if s_info["marks"] >= 90:
        f[s_id] = s_info
print(f)