n = int(input())
m = int(input())

matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    matrix.append(row)

for i in matrix:
    for j in i:
        print(j, end =' ')
    print()

print()

for i in range(m):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()