score = [34,87,55,79,80,90]

# Removing an Item Using the del Statement

del score[2]
print(score)

# Removing an Item Using the pop() Method
''' The pop() method removes the last item in a list, but it lets you work 
with that item after removing it. '''

score.pop()
poped_ele = score.pop()
print(score)
print(poped_ele)

# Removing an Item by Value

age = [45,19,19,20,49,90,78]
age.remove(19)
print(age)
for i in age:
    print(age.index(i))