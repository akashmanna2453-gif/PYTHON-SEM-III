def fibonacci():
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(9):
        c = a + b
        print(c)
        a = b
        b = c
print("Fibonacci series of 10 terms")
fibonacci()