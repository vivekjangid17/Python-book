'''  5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
 • If the list is empty, print the message We need to find some users!
 • Remove all of the usernames from your list, and make sure the correct message is printed. '''
 
user_names = ['admin', 'kanak', 'nisha', 'payal', 'devid']
for user in user_names:
    print(f'user: {user}')
    for user in user_names:
        user_names.pop()
else:
    print("We need to find some users!")
# for users in user_names:
#     user_names.remove()
    
print(user_names)

