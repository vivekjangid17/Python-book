# Returning a Simple Value

def get_formatted_name(first_name, last_name, middle_name):
    if first_name and middle_name and last_name:
        name = f'Your full name is {(first_name.title()).strip(" ")} {(middle_name.title()).strip(" ")} {(last_name.title()).strip(" ")}'

    elif first_name:
        name = ( f'Your first name is {(first_name.title()).strip(" ")}')

    elif middle_name:
        name = ( f'Your middle name is {(middle_name.title()).strip(" ")}')

    elif last_name:
        name = ( f'Your last name is {(last_name.title()).strip(" ")}')
    
    else:
        name = 'Please enter your name.'
        # print('Please enter your name.')

    return name


f_name = input("Enter your first name: ")
m_name = input("Enter your middle name: ")
l_name = input("Enter your last name: ")

full_name = get_formatted_name(f_name, l_name, m_name)
print(f"{full_name}")