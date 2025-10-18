n = int(input())
new_set = set()

for _ in range(n):
    s = input().lower()
    for j in range(len(s)):
        new_set.add(s[j])

print(len(new_set))



