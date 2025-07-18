n = int(input())
m = int(input())

mult = [[i*j for i in range(m)] for j in range(n)]


for i in mult:
    for j in i:
        print(j, end=' ')
    print()