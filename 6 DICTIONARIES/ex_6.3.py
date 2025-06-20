'''6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.'''

glossary = {
    'variable': 'A named location in memory used to store data that can be changed during program execution.',
    'function': 'A block of reusable code that performs a specific task when called.',
    'loop': 'A programming structure that repeats a block of code while a condition is true.',
    'list': 'A collection of ordered items that can hold a mix of data types and is changeable.',
    'dictionary': 'A collection of key-value pairs where each key is unique and is used to access its associated value.',
}

for key, value in glossary.items():
    print(f'{key}: {value}\n')