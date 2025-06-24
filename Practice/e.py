d = {}
l = [3,5,6,8]
for i in range(4):
    if i not in d:
        for j in l:
            d[i] = l[i]

print(d)
