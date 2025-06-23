'''6-12. Extensions: We're now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.'''

# Frequency Counter of Nested Elements: Given a list of dictionaries, count how many times each unique value appears (even inside nested dictionaries).

data = [
    {"name": "Alice", "info": {"age": 25, "city": "Delhi"}},
    {"name": "Bob", "info": {"age": 25, "city": "Mumbai"}},
    {"name": "Charlie", "info": {"age": 30, "city": "Delhi"}},
]

# Output: {'Alice': 1, 'Bob': 1, 'Charlie': 1, 25: 2, 30: 1, 'Delhi': 2, 'Mumbai': 1}

count = 0
for i in data:
    for k,v in i.items():
        if isinstance(v,dict):
            for n,p in v.items():
                print(f'{n}:{p}')
        else:
            print(f'{k}:{v}')
    print()
    