#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome To Random Password Generator")
nl=int(input("enter number of letter in password\n"))
nn=int(input("enter number of number in password\n"))
ns=int(input("enter number of symbol in password\n"))

password_list=[]

for i in range(1,nl+1):
    password_list.append(random.choice(letters))

for i in range(1,nn+1):
    password_list.append(random.choice(numbers))

for i in range(1,ns+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password=''
for i in password_list:
    password+=i
print(password)