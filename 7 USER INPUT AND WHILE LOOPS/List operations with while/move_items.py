# ************* Moving Items from One List to Another ***********

print("Using for loop...")
# Initial list of users to be confirmed
unconfirmed_users = ['alice', 'brian', 'candace']

# Already confirmed user
confirmed_users = ['vivek']

# ❗ This loop will not work as expected because we are modifying (popping) the list we are looping through
for u in unconfirmed_users:
    # Removes the last element from unconfirmed_users list each time (LIFO - last in, first out)
    user = unconfirmed_users.pop()
    
    # Displays which user is being verified
    print(f"Verifying user: {user.title()}")
    
    # Adds the popped user to the confirmed_users list
    confirmed_users.append(user)

# Final list of confirmed users
print(confirmed_users)

# ❗❗ IMPORTANT NOTE:
# This code does NOT confirm 'alice' because:
# - The 'for' loop uses the original list (3 items) to plan the loop.
# - But the list is being changed during the loop (pop removes items).
# - This shortens the list, so 'alice' is skipped before the loop reaches her.

# To fix this, use a 'while' loop instead:
print("\nUsing while loop...")

# Initial list of users to be confirmed
unconfirmed_users = ['alice', 'brian', 'candace']

# Already confirmed user
confirmed_users = ['vivek']

while unconfirmed_users:
    user = unconfirmed_users.pop()
    print(f"Verifying user: {user.title()}")
    confirmed_users.append(user)

print("\nThe following users have been confirmed:")
print(confirmed_users)