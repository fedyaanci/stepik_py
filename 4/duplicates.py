a = input()

first_list = list(a.split())

temp_list = []
res_list = []
count = 1
j = 0

for i in range(1, len(first_list)):

    if first_list[i] == first_list[i-1]:
        count +=1
    elif first_list[i] != first_list[i-1]:
        res_list.append([first_list[i-1]]*count)
        count = 1

    if  i+1 == len(first_list):
        if first_list[i] == first_list[i-1]:
            res_list.append([first_list[i-1]]*count)
        else:
            res_list.append([first_list[i]]*count)

print(res_list)
