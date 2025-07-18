n = int(input())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for j in range(n):
        matrix[j][j], matrix[n-1-j][j] = matrix[n-1-j][j], matrix[j][j] 
        
for i in matrix:
    for j in i:
            print(j, end=' ')
    print()