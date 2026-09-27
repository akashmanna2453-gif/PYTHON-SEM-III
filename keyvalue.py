d = {'b': 2, 'a': 3, 'c': 1, 'd': 3}

bykeys = sorted(d.items())

byvalues = sorted(d.items(), key=lambda kv: kv[1])

byvaluesthenkeys = sorted(d.items(), key=lambda kv: (kv[1], kv[0]))

bykeysthenvalues = sorted(d.items(), key=lambda kv: (kv[0], kv[1]))

print("By keys:", bykeys)
print("By values:", byvalues)
print("By values then keys:", byvaluesthenkeys)
print("By keys t