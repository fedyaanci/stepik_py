a = input()

stroka = 'Р'
counter = 0
max_counter = 0

for i in a:
    if i == 'Р':
        counter += 1
    else:
        max_counter = max(counter, max_counter)
        counter = 0
max_counter = max(counter, max_counter)
print(max_counter)