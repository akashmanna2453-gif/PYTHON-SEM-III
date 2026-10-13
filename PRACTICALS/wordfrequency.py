s = "python is not for begineers"
result = {w:s.split().count(w) for w in set(s.split())}
print(result)