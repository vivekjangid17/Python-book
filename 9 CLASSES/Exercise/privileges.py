'''9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges'''



class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print("-", privilege)   
            
class Admin:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.privileges = Privileges()
             
if __name__ == "__main__":            
    admin1 = Admin("Vivek", "Jangid")
    admin1.privileges.show_privileges()