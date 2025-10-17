# Pass by reference

class Customer:
    
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        
    
def greet(customer):
    # if customer.gender == 'Male':
    #     print(f"Hello, {customer.name} Sir")
    # else:
    #     print(f"Hello, {customer.name} Ma'am")
    
    # cust2 = Customer("Payal", "Female")
    
    # return cust2
    
    # print(id(customer))
    
    customer.name = "Baby"
    print(customer.name)

cust = Customer("Bhavik", "Male")
# new_customer = greet(cust)
# print(new_customer.name)
# greet()
greet(cust)
# print(id(cust))

print(cust.name)