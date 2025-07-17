n = int(input())

list1 = []

for i in range(1,n+1):
    list1.append(list(range(1,i+1)))

for i in list1:
    print(i)
