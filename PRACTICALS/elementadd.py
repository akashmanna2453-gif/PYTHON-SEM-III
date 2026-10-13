t1 = (1,2,3)
t2 = (4,5,6)
result = tuple(a+b for a,b in zip(t1,t2))
print(result)