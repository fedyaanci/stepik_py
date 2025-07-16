count = int(input())
num_list = []

for i in range(count):
    num_list.append(int(input()))

main_num = int(input())
flag = False

for i in range(len(num_list)-1):
    first_mn = num_list[i]
    if first_mn != 0:
        search_mn = (main_num / first_mn)
    else:
        continue 

    if ((search_mn in num_list and num_list.count(num_list[i]) > 1) or (search_mn in num_list and search_mn != first_mn)):
        print('ДА')
        flag = True
        break
    
if flag == False:
    print('НЕТ')