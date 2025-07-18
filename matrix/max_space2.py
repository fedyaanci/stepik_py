n = int(input())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    if len(row) != n:
        print(f'Некорректный ввод- матрица {n} x {n}')
    matrix.append(row)
 

def max_space(matrix):
    max_elem = matrix[0][0]
    for i in range(n):
        for j in range(n):
            if (i>=j and i <= n -1 -j) or (j>=i and i >= n-1-j):
                max_elem = max(max_elem, matrix[i][j])
    return max_elem

print(max_space(matrix))