s = input().lower().split(' ')

for i in range(len(s)):
    s[i]=s[i].strip('/.,!?')

print(s)
sset = set(s)
print(sset)
print(len(sset))
