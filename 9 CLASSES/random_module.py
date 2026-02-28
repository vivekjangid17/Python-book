import random 

# Example 1: Pick a Random Element from a List
a = [1, 2, 3, 4, 5, 6]
print(f'Choosing a random number from list: {random.choice(a)}')

# Example 2: Using seed() for Reproducible Output
# random.seed(1)

# Example 3: Generate Random Integers in a Range
random_num = random.randint(1,100)
print(f'Random number btw 1 to 100: {random_num}')

# Example 4: Generate a Random Float Between 0 and 1
print(f'Generate random floats between 0.0 to 1: {random.random()}')

# Example 6: Select Multiple Unique Random Items
print(f'Select multiple items: {random.sample(a,4)}')

# Example 7: Shuffle Elements in a List
print("Before shuffle a:",a)
random.shuffle(a)
print(f'After shuffle a: {a}')