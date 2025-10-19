m1 = set(map(int, input().split()))
m2 = set(map(int, input().split()))
m3 = set(map(int, input().split()))

m4 = set(range(10 + 1))

sset = sorted(list(m4-(m1|m2|m3)), key=int, reverse=False)
for i in sset:
    print(i, end=' ')