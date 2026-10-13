list1 = [(1,2),(2,3),(5,6)]
list2 = [(9,2),(2,3),(5,6)]
result = [t for t in list1 if t in list2]
print(result)