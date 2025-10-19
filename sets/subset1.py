sset1 = set(input())
sset2 = set(input())

# print('NO') if sset1.isdisjoint(sset2) else print('YES')

print("YES") if sset1.issuperset(sset2) else print('NO')
