'''6. Top N Frequent Words in a Dictionary of Sentences
Given a dictionary where keys are IDs and values are sentences, return the top N most frequent words.'''

data = {
    1: "hello world hello",
    2: "world of python",
    3: "hello python hello"
}
N = 2

# Top 2 frequent words -> [('hello', 4), ('world', 2)]


# Step 1: Create a list of values as strings 
combine = []
for key, value in data.items():
    # print(f"{key}: {value}")
    if key not in combine:
        combine.append(value)
print(combine)

# Step 2: Spit the words of list(combine) of string 
words = []
for c in combine:
    words.extend(c.split())
print(words)

# Step 3: Count the frequency of words in list words[]
freq = {}
for i in words:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

# Step 4: Convert dict to list of (word, frequency) tuples
items = []
for word, count in freq.items():
    items.append((word,count))
print(items)

# Step 4: Prints top 2 most frequent words
print(items[:2])


# More simple code
# word_freq = {}

# # Step 1: Count word frequencies
# for sentence in data.values():
#     words = sentence.split()
#     for word in words:
#         if word in word_freq:
#             word_freq[word] += 1
#         else:
#             word_freq[word] = 1