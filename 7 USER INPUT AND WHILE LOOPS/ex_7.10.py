'''7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.'''

result = {}
active_poll = True
while active_poll:
    name = input("Enter your name: ")
    place = input("If you could visit one place in the world, where would you go? ")
    
    result[name] = place

    repeat = input("Do you want to add another response!(yes/no)")
    if repeat == 'no':
        active_poll = False
    
for key, value in result.items():
    print(f"My name is {name.title()}. \nI would like to visit {place.title()}.")
