current_users = ['John', 'Kanak', 'nisha', 'motu', 'patlu']
new_users = ['pragati', 'nisha', 'jaden', 'devid', 'john']
    
current_users_lower = [user.lower() for user in current_users]
for i in new_users:
    if i.lower() in current_users_lower:
        print("User needs to enter a new username.")
    else:
        print("Username is available.")
