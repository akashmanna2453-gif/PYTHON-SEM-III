import random
import string
length = int(input("Enter length of a password: "))
character = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(length):
    password += random.choice(character)
print("Generated Password: ",password)