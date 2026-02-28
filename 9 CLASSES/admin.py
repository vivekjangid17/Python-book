'''9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator's set of privileges. Create an instance of Admin, and call your method'''


from user import User


class Admin(User):
    
    def __init__(self):
        
        import privileges    # this is done for ex_9.08
        
        # super().__init__(first_name, last_name, age, email, city)
        self.privileges = ["can add post", "can delete post", "can ban user"]
        self.privilege = privileges.Privileges()        # this is done for ex_9.08
        
    def show_privileges(self):
        print("Here are the administrator's privilages..")
        for privilege in self.privileges:
            print(privilege)

if __name__ == "__main__":        
    admin = Admin()
    admin.show_privileges()
    admin.privilege.show_privileges()        # this is done for ex_9.08
