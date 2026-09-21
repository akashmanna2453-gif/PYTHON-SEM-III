a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("before swapping: a =", a, "b =", b)
c = a
a = b
b = c
print("after swapping: a =", a, "b =", b)  # without function and multiple assignment

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("before swapping: a =", a, "b =", b)
a ,b = b ,a  # with multiple assignment
print("after swapping: a =", a, "b =", b)
