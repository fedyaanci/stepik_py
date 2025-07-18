n = int(input())
m = int(input())

def create_matrix(n,m):
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))

        if len(row) != m:
            print('error')
            exit()

        matrix.append(row)
    return matrix

def table_max(matrix):
    max_elem = max(matrix)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == max_elem:
                return [i, j]
            else:
                return -1

matrix=create_matrix(n,m)

res= table_max(matrix)

if res != -1:
    for i in res:
        print(i, end = ' ')
else:
    print('error')