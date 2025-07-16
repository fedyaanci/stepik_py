weight = float(input())
height = float(input())

imt = float(weight/(height**2))

if imt < 18.5:
    print('Недостаточная масса')
elif imt > 25:
    print('Избыточная масса')
else:
    print('Оптимальная масса')