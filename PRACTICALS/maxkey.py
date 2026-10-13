d = {'a':1,'b':2,'c':3}
result = max(d,key=d.get)
print(result)