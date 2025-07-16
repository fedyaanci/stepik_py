a = [int(i) for i in input().split()]

# что должны поменять запоминаем
#biginning data
# 1 2 3 4 5 -> temp =1  5 2 3 4 5 --> temp=2 

def shift(a):
    for i in range(len(a)):
        if i==0:
            temp=a[i]
            a[i]=a[i-1]
        else:
            temp, a[i] = a[i], temp
    return a

a = shift(a)

for i in a:
    print(i, end = ' ')