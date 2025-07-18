n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Поворот матрицы на 90 градусов по часовой стрелке
rotated = [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]

# Вывод результата
for row in rotated:
    print(' '.join(map(str, row)))