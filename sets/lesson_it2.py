m1 = set(input().split())
m2 = set(input().split())
m3 = set(input().split())

sset = sorted(list((m1|m2|m3)-(m1&m2&m3)),key=int)

for i in sset:
    print(i,end=' ')