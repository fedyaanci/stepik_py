s = input().lower().split(' ')

for i in range(len(s)):
    s[i]=s[i].strip('/.,!?')

sset = set(s)
print(len(sset))
