n = int(input("Enter a number"))
n2 = n
s = 0
while n != 0:
    d = n % 10
    s = s + d*d*d
    n = n // 10
if n2 == s:
    print("It is a amstrong number")
else:
    print("It is not a amstrong number")