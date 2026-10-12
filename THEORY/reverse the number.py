n=int(input("Enter a number:"))
n2 = n
r = 0
while n != 0:
    d = n % 10
    r = r * 10 +d
    n = n // 10
print("Reversed number",r)
if n2 == r:
    print("It is a palindrome")
else:
    print("It is not a palindrome")