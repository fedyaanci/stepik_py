n = int(input())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

def bool_sym(matrix):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == matrix[j][i]:
                out = 'YES'
            else:
                return 'NO'
                
    return out

print(bool_sym(matrix))