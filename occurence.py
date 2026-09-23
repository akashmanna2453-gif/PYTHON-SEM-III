s = "success"
count = {}
for ch in s.lower():
    if ch.isalpha():
        count[ch] = count.get(ch,0) + 1
print("Count of occureence in letter is ", count)