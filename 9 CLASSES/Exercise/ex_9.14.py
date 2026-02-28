'''9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.'''

'''9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.'''

import random

# Lottery pool
lottery_items = [3, 7, 12, 25, 34, 41, 56, 68, 72, 90,
                 'A', 'B', 'C', 'D', 'E']

# Your ticket (choose any 4 items from above list)
my_ticket = [3, 'A', 41, 7]

attempts = 0
won = False

while not won:
    attempts += 1
    winning_ticket = random.sample(lottery_items, 4)

    if winning_ticket == my_ticket:
        won = True

print("🎉 You won the lottery!")
print("Your ticket:", my_ticket)
print("Winning ticket:", winning_ticket)
print("It took", attempts, "tries to win.")