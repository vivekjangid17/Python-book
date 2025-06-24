'''5. Dictionary to Flattened Dot-Notation
Flatten a nested dictionary using dot notation for keys.'''

data = {
    "name": "Alice",
    "address": {
        "city": "Delhi",
        "pin": 110001
    }
}

# Output: {'name': 'Alice', 'address.city': 'Delhi', 'address.pin': 110001}

# Flatten ⇒ remove nesting → create a single, top-level collection.

flatten = {}

for key, value in data.items():
    if isinstance(value,dict):
        for inner_key,inner_value in value.items():
            # create a new_key using dot notation between key and inner_key
            new_key = key + '.' + inner_key
            # create a new key-value pair in flatten dictionary with new_key
            flatten[new_key] = inner_value
    else:
        # add the outer key and value pair to the flatten dictionary
        flatten[key] = value
print(flatten)