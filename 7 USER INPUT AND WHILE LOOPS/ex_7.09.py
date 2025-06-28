'''7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.'''

sandwich_orders = [
    "pastrami",
    "tuna sandwich",
    "grilled cheese sandwich",
    "egg sandwich",
    "pastrami",
    "club sandwich",
    "veggie sandwich",
    "pastrami",
    "ham and cheese sandwich"
]

print("The deli has run out of pastrami.")


finished_sandwiches = []

while 'pastrami' in finished_sandwiches:
    finished_sandwiches.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)

# Step 4: Print all the sandwiches that were made
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
