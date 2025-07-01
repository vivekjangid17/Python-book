# Returning a Dictionary

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age

    return person


while True:
    print("\nPlease tell me about your self:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    age = int(input("Age: "))
    if age == 'q':
        break
    name = build_person(f_name,l_name,age)
    print(name)