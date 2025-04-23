'''Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:'''

my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

# Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
print("The first three items in the list are:")
print(my_foods[:3])
    
# Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
print("\nThree items from the middle of the list are:")
print(my_foods[1:4])

# Print the message The last three items in the list are:. Use a slice to print the last three items in the list.
print("\nThe last three items in the list are:")
print(my_foods[-3:])