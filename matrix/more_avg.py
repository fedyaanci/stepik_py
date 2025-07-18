n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    avg = sum(matrix[i])/n
    counter=0
    for j in range(n):
        if matrix[i][j]>avg:
            counter+=1 
    print(counter)