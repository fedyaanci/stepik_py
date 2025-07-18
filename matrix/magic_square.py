n = int(input())
matrix = []
diagonals = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

rotated = [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]

for i in range(n):
    diagonals.append()

for i in range(n-1):
    if (sum(rotated[i]) == sum(rotated[i])) and (sum(matrix[i]) == sum(matrix[i+1])):
        flag = 'YES'
    else:
        flag = 'NO'

for i in range(n):
    sum =  matrix[i][i]
    

for i in range(n):
    sum_h = sum(matrix[i])
    for j in range(n):
        sum_v = sum_v + 