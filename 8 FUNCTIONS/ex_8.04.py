'''8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.'''


def make_shirt(message,size=45):
    print(f'The size if the shirt is {size} and the message that should be printed is {message}.')


make_shirt("I love Python")   # positional arguments
make_shirt(size=18,message="Virat Kohli")   # keyword arguments