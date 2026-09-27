d = {'b': 2, 'a': 3, 'c': 1, 'd': 3}

bykeys = sorted(d.items())

byvalues = sorted(d.items(), key=lambda kv: kv[1])

byvaluesthenkeys = sorted(d.items(), key=lambda