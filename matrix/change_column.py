n = int(input())
m = int(input())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

c1,c2= map(int,input().split())

for i in range(n):
    matrix[i][c1], matrix[i][c2] = matrix[i][c2], matrix[i][c1]

for i in matrix:
    for j in i:
        print(j,end=' ')
    print()