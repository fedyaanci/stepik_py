
a = list(map(str, input().split(' ')))
n = int(input())
new_list = [[] for _ in range(n)]

for i in range(0, len(a), ):
    column = i%n
    new_list[column].append(a[i])


print(new_list)
    