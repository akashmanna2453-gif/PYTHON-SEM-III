n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" \n")

    temp = a
    a = b
    b = temp + b