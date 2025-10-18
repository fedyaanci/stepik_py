s1 = set(map(int,input().split()))

s2 = set(map(int,input().split()))

s3 = sorted(list(s1-s2))

for i in s3:
    print(i, end = ' ')