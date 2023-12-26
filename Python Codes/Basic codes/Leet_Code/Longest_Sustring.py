s = 'cbbd'
new_s = []
for i in range(0, len(s)):
    new_s.append(s[i:] + s[:i])

print(new_s)