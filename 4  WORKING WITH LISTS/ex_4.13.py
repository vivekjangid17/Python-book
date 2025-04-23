
foods = ('pizza', 'burger', 'samosa', 'patiez', 'momos')
print("Original menu")
for food in foods:
    print(food)

# TypeError: 'tuple' object does not support item assignment
# foods[1] = 'kachori'

foods = ('pizza', 'burger', 'kachori', 'patiez', 'roti')
print("\nUpdated menu")
for food in foods:
    print(food)