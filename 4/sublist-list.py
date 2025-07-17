a = list(input().split())
#range не включает последнее число
def sublist(a):
    temp_list = []
    left = 0
    right = 1 
    raznitsa = 1
    temp_list.append([])
    while raznitsa < len(a) + 1:
        if a[left:left+raznitsa]:
            temp_list.append(a[left:left+raznitsa])
        left +=1
        if left+raznitsa == len(a)+1:
            left = 0
            raznitsa +=1
    return temp_list

new = sublist(a)
print(new)