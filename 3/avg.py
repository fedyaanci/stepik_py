list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0

for i in list1:
    counter += len(i)
    for j in i:
        total += j

total = 0
counter = 0

for i in list1:
    counter +=len(i)
    total +=sum(i)

total = 0
counter = 0

total = sum([sum(i) for i in list1])
counter = sum([len(i) for i in list1])
print(total/counter) 