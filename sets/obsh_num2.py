n = int(input())
sset = set()

for i in range(n):

    temp = set(input())
    
    if (i == 0):
        sset |= temp
    else:
        sset &= temp

for i in sorted(list(sset)):
    print(i, end=' ')


