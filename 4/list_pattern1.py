# На вход программе подается число 
# n
# n. Напишите программу, которая создает и выводит построчно список, состоящий из 
# n
# n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].


#1-list
#1)
#a = [int(i) for i in input().split()]
#2)
# a=[]
# for i in range(5):
#     a.append(int(input()))
# print(a)
#2  a = list(map(int, input().split()))


#2-list

# a = []

# for _ in range(5):
#     a.append([0]*m)
# n = int(input())

# list1 = []

# for i in range(1,n+1):
#     list1.append(i )

n = int(input())

list = [[ int(i) for i in range(1,n+1)] for _ in range(n)]
print(list)