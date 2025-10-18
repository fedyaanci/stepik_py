s1=set(input().split()) 
s2=set(input().split())

s3 = sorted(list(s1 & s2))

for i in s3:
    print(i, end=' ')
