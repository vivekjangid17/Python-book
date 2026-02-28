#  5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif else chain.
#  • If the alien is green, print a message that the player earned 5 points.
#  • If the alien is yellow, print a message that the player earned 10 points.
#  • If the alien is red, print a message that the player earned 15 points.                                       #  • Write three versions of this program, making sure each message is printed for the appropriate color alien.

a = input("Enter color: ")

alien_color = a
if alien_color == "green":
    print("Players earned 5 points.")
elif alien_color == "yellow":
    print("Players earned 10 points.")
else:
    print("Players earned 15 points.")