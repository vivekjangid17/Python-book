import random

random_number = random.randrange(100)

while(True):

    nguess = int(input("Guess a number(1-100): "))
    if nguess < random_number:
        print("Greater number please...")
    elif nguess > random_number:
        print("Smaller number please...")
    elif nguess == random_number:
        print("Congratulations, You find the random number.")
        break
    
