def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        print(f"Full name: {first_name} {middle_name} {last_name}")
    else:
        print(f"Full name: {first_name} {last_name}")
    
f_name = input("Enter your first name: ")
m_name = input("Enter your middle name: ")
l_name = input("Enter your last name: ")

get_formatted_name(f_name, m_name, l_name)
    