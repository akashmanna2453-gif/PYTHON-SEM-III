def fibo(n):
    a,b=0,1
    for i in range (0,n):
        print(a,"")
        a,b=b,a+b
print("Fibonaaci Series:")
n = int(input("Enter a number"))
print(fibo(n))
