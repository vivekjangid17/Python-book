# dictionary using dict() method
person = dict(name="Madhav", age=20, city="Delhi")
print(person)

# using a list of tuples
student = dict([("name","Madhav"), ("age",20), ("grade", "A")])
print(student)
print(student["name"])

# add a new key-value pair
student["email"] = "madhavs34@gmail.com"
print(student)

print(student.get("city", "city is not the key"))

# delete a pair
del student["age"]
print(student)

g = student.pop("grade")
print(student)
print(g)