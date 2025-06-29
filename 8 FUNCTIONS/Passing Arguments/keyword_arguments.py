# Keyword Arguments

def full_name(f_name,l_name):
    print(f'My full is {f_name} {l_name}.')


full_name(f_name='Vivek',l_name='Jangid')
full_name(l_name='Jangid',f_name='Vivek')   # Order does not Matters in Keyword Arguments

# Default Values
def address(district, state = 'Rajasthan'):
    print(f"My address is {district}, {state}.")


address(district='Alwar')
address(district='Gajiyabad',state="UP")
address('Alwar')

# When ywe use default values, any parameter with a default value needs to be listed after all the parameters that don't have default values. This allows Python to continue interpreting positional arguments correctly.