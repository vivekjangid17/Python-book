# 3. Merge Multiple Dictionaries by Adding Values
# Merge the following dictionaries by adding values for the same keys.

dicts = [
    {"a": 10, "b": 20},
    {"a": 5, "c": 15},
    {"b": 10, "c": 5}
]

# Output: {'a': 15, 'b': 30, 'c': 20}

freq = {}
for d in dicts:
    for key, value in d.items():
        if key in freq:
            # if key is present in the freq dictionary then add the value 
            freq[key] += value
        else:
            freq[key] = value
        
print(freq)
        

        
