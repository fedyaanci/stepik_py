n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

def max_space(matrix):
    max_elem = matrix[0][0]
    for i in range(n):
        for j in range(n):
            if i >= j:
                max_elem = max(max_elem, matrix[i][j])
    return max_elem

print(max_space(matrix))
