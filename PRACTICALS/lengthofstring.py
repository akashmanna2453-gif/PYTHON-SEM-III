strings = ["akash", "arif", "level", "level"]
count = 0
matched = []

for s in strings:
    if len(s) > 1 and s[0] == s[-1]:
        count += 1
        matched.append(s)

print(f"Total strings with same first and last character: {count}")
print(f"Matched strings: {matched}")