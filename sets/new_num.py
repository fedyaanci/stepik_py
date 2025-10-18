s = input().split()

set_num = set()

for i in s:
    if i.strip('0') in set_num:
        print('Yes')
    else:
        print('No')
    set_num.add(i)
