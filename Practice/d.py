c = "Alice"

d = {"name": "Alice", "info": {"age": 25, "city": "Delhi"}}
for i,j in d.items():
    if c in (i,j):
        print(c)

f = d['info']
print([f])