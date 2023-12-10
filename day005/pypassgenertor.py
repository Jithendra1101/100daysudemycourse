import random 
import string
print("\n*********************welcome to pypassword generator******************\n")
letters = list(string.ascii_lowercase + string.ascii_uppercase)
numbers = list(map(str, range(10)))
characters = ['@','#','$','%','&','*']
n_letters = int(input("how many letters would you like in your password? "))
n_numbers = int(input("how many numbers would you like in your password? "))
n_characters = int(input("how many characters would you like in your password? "))
''' easy method '''

password = ""
for i in range(1,n_letters+1) : 
    password += random.choice(letters)
for i in range(1,n_numbers+1) :
    password += random.choice(numbers)
for i in range(1,n_characters+1) :
    password += random.choice(characters)
print("your password is : "+ password)    

''' hard method '''
password = []
for i in range(1,n_letters+1) : 
    password.append(random.choice(letters))
for i in range(1,n_numbers+1) :
    password.append(random.choice(numbers))
for i in range(1,n_characters+1) :
    password.append(random.choice(characters))
random.shuffle(password)
password_c = ""
for char in password :
    password_c +=char
print("your genreterd password is :" + password_c)    
    



