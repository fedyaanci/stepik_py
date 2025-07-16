list_num = [int(i) for i in input().split()]

for i in range(0,len(list_num)-1,2):
    list_num[i], list_num[i+1] = list_num[i+1], list_num[i]

for i in list_num:
    print(i, end = ' ')
