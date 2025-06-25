
print("You are going to play a game...")
inp = input("quit or continue...\n")
if inp == 'q':
    print("Are you sure you want to quit the game!(y or n)")
    a_in = input()
    if a_in == 'y':
        print("Thanks for playing game.")
    elif a_in == 'n':
        print("Let's continue the game...")
    else:
        print("Please make sure you want to quit or continue.")
else:
    print("Continue")
