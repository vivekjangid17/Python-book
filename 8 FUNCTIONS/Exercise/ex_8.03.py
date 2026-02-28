'''8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.'''

def make_shirt(size, message):
    print(f'The size if the shirt is {size} and the message that should be printed is {message}.')


make_shirt(18,"Virat Kohli")   # positional arguments
make_shirt(size=18,message="Virat Kohli")   # keyword arguments