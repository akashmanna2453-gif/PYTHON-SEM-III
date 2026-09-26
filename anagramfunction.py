def anagram(a, b):
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
    
    return sorted(a) == sorted(b)


a = input("Enter first word: ")
b = input("Enter second word: ")

if anagram(a, b):
    print("Anagram")
else:
    print("Not anagram")