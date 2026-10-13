s = input("Entet a string: ")
alpha = "abcdefghijklmnopqrstuvwxyz"
for ch in alpha:
    if ch not in s.lower():
        print("Not a pangram")
        break
else:
    print("Pangram")