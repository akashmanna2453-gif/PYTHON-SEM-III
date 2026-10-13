import random
import string
password = ""
characters = string.ascii_letters + string.digits + string.punctuation
for i in range (10):
    password = password + random.choice(characters)
print(password)