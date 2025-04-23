players = ['rohit', 'kohli', 'pant', 'dhoni', 'rahul']
print(players[0:3])
print(players[:4])
print(players[2:])

#  Looping Through a Slice
players = ['rohit', 'kohli', 'pant', 'dhoni', 'rahul']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    
