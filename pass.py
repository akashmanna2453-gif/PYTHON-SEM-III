import random

def password():
    chars = "ABCabc123@#"
    return "".join(random.choice(chars) for i in range(8))

print("Password:", password())