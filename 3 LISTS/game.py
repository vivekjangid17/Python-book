# aliens = ['Raju', 'Sanju', 'Anil', 'Karan', 'Satish', 'Gopal']
aliens = [1,2,3,4,5,6,8]

shot = input("Enter a no: ")
for i in aliens:
    if aliens[i] == shot:
        aliens.remove(aliens[i])
print(aliens)
        