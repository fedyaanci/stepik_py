num = input()
num_list = list(num)
counter = 0
res = ''
first_sign = num[0]
for i in range(len(num)-1, 0, -1):
    res = res + num[i]
    counter += 1 
    if counter == 3:
        res = res + ','
        counter = 0
       
new_res = res[::-1]

print(first_sign+new_res)