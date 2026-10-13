s1 = input("Enter")
s2 = input("Enter")
result = sorted(s1) == sorted(s2)
print("anagram" if result else "not anagram")