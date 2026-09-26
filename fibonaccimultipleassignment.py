n = int(input("Enter number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" \n")
    a, b = b, a + b