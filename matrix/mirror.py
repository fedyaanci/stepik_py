n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        print(matrix[n-1-i][j], end = ' ')
    print()