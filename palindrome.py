n = int(input("Enter a number: "))
n2 = n
r = 0
while n != 0:
    d = n % 10
    r = r * 10 + d
    n = n // 10
if r == n2:
    print("It is a palindrome")
else:
    print("Not a palindrome")