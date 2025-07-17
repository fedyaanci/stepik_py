my_list = [[0], [1, 2], [3, 4, 5]]

#1
n = 3
m = 5
list1 = []

for _ in range(n):
    list1.append([0]*m)
print(list1)

#list1[1][1] = 1
#print(list1)

#2

list1 = [[0]*m for _ in range(n)]