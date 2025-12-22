import random
import string
pass_given = int(input("Enter the length of the password: "))

def generate_password(length):
    #combining alphabets(upper and lower), number and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    #randomly selecting k numbers of characters
    password = ''.join(random.choices(characters, k=length))
    return password

password = generate_password(pass_given)
print(password)
