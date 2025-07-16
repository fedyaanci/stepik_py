n = int(input())

dict = {'Первая четверть' : 0,
        'Вторая четверть' : 0,
        'Третья четверть' : 0,
        'Четвертая четверть' : 0}

for _ in range(n):
    x, y = map(int, input().split())
    if (x>0 and y>0):
        dict['Первая четверть'] += 1
    if (x<0 and y>0):
        dict['Вторая четверть'] +=1
    if (x<0 and y<0):
        dict['Третья четверть'] +=1
    if (x>0 and y<0):
        dict['Четвертая четверть'] +=1

for key, value in dict.items():
    print(f'{key}: {value}')
