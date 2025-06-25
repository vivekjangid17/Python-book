'''6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.'''

glossary = {
    'variable':
    'A named location in memory used to store data that can be changed during program execution.',
    'function':
    'A block of reusable code that performs a specific task when called.',
    'loop':
    'A programming structure that repeats a block of code while a condition is true.',
    'list':
    'A collection of ordered items that can hold a mix of data types and is changeable.',
    'dictionary':
    'A collection of key-value pairs where each key is unique and is used to access its associated value.',
    'recursion':
    'A function that calls itself to solve smaller instances of a problem.',
    'immutable':
    'An object whose state cannot be modified after it\'s created, like a tuple in Python.',
    'syntax':
    'The set of rules that defines how a program must be written for the computer to understand.',
    'iterator':
    'An object that allows you to loop over elements one at a time using `next()`.',
    'encapsulation':
    'A principle in OOP where data and methods are bundled together to restrict direct access.'
}

for key, value in glossary.items():
    print(f'{key}: {value}\n')
