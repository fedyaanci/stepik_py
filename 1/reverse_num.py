num = input()

def reverse_num(num):
    temp_num = num[::-1]
    flag = 'f'
    while flag == 'f':
        if temp_num[0] != '0':
            return int(temp_num)
        else:
            temp_num = temp_num[1::]
    return temp_num

def strange_reverse_num(num):
    
    temp_num = num[0:-5:1] + num[-1:-6:-1]
    temp_list = list(temp_num)
    for i in range( len(temp_list) - 1 ):
        if temp_list[i] != 0:
            return int(''.join(temp_list))
        else:
            del temp_list[i]
        

#print(reverse_num(num))

print(strange_reverse_num(num))