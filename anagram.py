str1 = input("Enter a string: ")
str2 = input("Enter a string: ")
if sorted(str1) == sorted(str2):
    print("anagram")
else:
    print("Not anagram")
