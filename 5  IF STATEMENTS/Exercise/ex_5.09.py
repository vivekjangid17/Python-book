'''  5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
 • If the list is empty, print the message We need to find some users!
 • Remove all of the usernames from your list, and make sure the correct message is printed. '''
 

user_names = ['admin', 'kanak', 'nisha', 'payal', 'devid']

user_names.clear()  # Clear the list to simulate an empty list

if user_names:
    for user in user_names:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")