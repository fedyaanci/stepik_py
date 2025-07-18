n = int(input())
m = int(input())

matrix = []
temp_list = []

for i in range(n):
    row = []
    for j in range(m):
        value = input()
        row.append(value)
    matrix.append(row)

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()
