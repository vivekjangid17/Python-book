# Dictionary Key Swap with Value Collisions: Swap keys and values in a dictionary. If values are not unique, store multiple keys as a list.

data = {
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 3
}

# Output: {1: ['a', 'c'], 2: ['b'], 3: ['d']}

# print(data)
# creating empty dictionary
frequency = {}
for key, value in data.items():
    # swap key-value
    new_key, new_value = value, key
    print(f"{new_key}:{new_value}")

    # if condition checks if the new_key(value) present in the frequency{} dictionary
    if new_key in frequency:
        # Go to the dictionary frequency, find the list stored at new_key, and append (add) new_value to that list."
        frequency[new_key].append(new_value)
    else:
        # Add a new key to the dictionary frequency (called new_key) and store a list with one item new_value as its value.
        frequency[new_key] = [new_value]
print(frequency)


# empt ={}
# for key, value in data.items():
#     # swap key, value
#     # temp = key
#     # key = value
#     # value = temp

#     key, value = value, key
#     print(f'{key}:{value}')

#     if key in data:
#         empt[key] += 1
#     empt[key] = 1
# print(empt)
