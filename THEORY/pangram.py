sent = input("Enter a sentence: ")
alpha = "abcdefghijklmnopqrstuvwxyz"
for char in alpha:
    if char not in sent.lower():
        print("Not The quick brown fox jumps over the lazy dogPangram")
else:
    print("Pangram")