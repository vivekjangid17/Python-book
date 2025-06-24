'''6-12. Extensions: We're now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.'''

# Frequency Counter of Nested Elements: Given a list of dictionaries, count how many times each unique value appears (even inside nested dictionaries).

data = [
    {"name": "Alice", "info": {"age": 25, "city": "Delhi"}},
    {"name": "Bob", "info": {"age": 25, "city": "Mumbai"}},
    {"name": "Charlie", "info": {"age": 30, "city": "Delhi"}},
]

# Output: {'name': 3, 'Alice': 1, 'info': 3, 'age': 3, 25: 2, 'city': 3, 'Delhi': 2, 'Bob': 1, 'Mumbai': 1, 'Charlie': 1, 30: 1}

# Sample nested dictionary data
data = [
    {"name": "Alice", "info": {"age": 25, "city": "Delhi"}},
    {"name": "Bob", "info": {"age": 25, "city": "Mumbai"}},
    {"name": "Charlie", "info": {"age": 30, "city": "Delhi"}},
]

# Creating an empty dictionary to store the frequency of keys and values
frequency = {}

# Loop through each dictionary (person) in the list
for person in data:
    
    # Loop through each key and value in the outer dictionary
    for outer_key, outer_value in person.items():
        
        # Count the outer key (like 'name', 'info')
        if outer_key in frequency:
            frequency[outer_key] += 1
        else:
            frequency[outer_key] = 1

        # If the value is another dictionary (like the value of 'info')
        if isinstance(outer_value, dict):
            
            # Loop through nested key-value pairs (like 'age': 25)
            for nested_key, nested_value in outer_value.items():
                
                # Count the nested key (like 'age', 'city')
                if nested_key in frequency:
                    frequency[nested_key] += 1
                else:
                    frequency[nested_key] = 1

                # Count the nested value (like 25, 'Delhi')
                if nested_value in frequency:
                    frequency[nested_value] += 1
                else:
                    frequency[nested_value] = 1
        
        else:
            # If the outer value is not a dictionary (like 'Alice'), count it
            if outer_value in frequency:
                frequency[outer_value] += 1
            else:
                frequency[outer_value] = 1

# Print the final frequency dictionary
print(frequency)
