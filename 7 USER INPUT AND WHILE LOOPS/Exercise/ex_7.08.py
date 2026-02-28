'''7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.'''

sandwich_orders = [
    "tuna sandwich",
    "grilled cheese sandwich",
    "egg sandwich",
    "club sandwich",
    "veggie sandwich",
    "ham and cheese sandwich"
]

finished_sandwiches = []

for sandwich in sandwich_orders[:]:
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)

# Step 4: Print all the sandwiches that were made
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
