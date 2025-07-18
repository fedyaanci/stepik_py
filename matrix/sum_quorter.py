n = int(input())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    if len(row) != n:
        print(f'Некорректный ввод- матрица {n} x {n}')
    matrix.append(row)
 
def max_space(matrix):
    dict_quorter = {'Верхняя четверть': 0,
                    'Правая четверть': 0,
                    'Нижняя четверть': 0,
                    'Левая четверть': 0}
    
    for i in range(n):
        for j in range(n):
            if (i > j and i < n - 1 - j):
                dict_quorter['Левая четверть'] += matrix[i][j]
            if (j > i and i > n-1-j):   
                dict_quorter['Правая четверть'] += matrix[i][j]
            if (i < j and i < n-1-j):
                dict_quorter['Верхняя четверть'] += matrix[i][j]
            if (i > j and i > n-1-j):
                dict_quorter['Нижняя четверть'] += matrix[i][j]
    return dict_quorter

dict_quorter = max_space(matrix)

for key, value in dict_quorter.items():
    print(f'{key}: {value}')
