n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))


def track(matrix):
    sum = 0
    for i in range(n):
        for j in range(n):
            if i==j: 
                sum +=matrix[i][j]
    return sum

print(track(matrix))