a = input().split()
n = int(input())

def chunked(a,n):
    temp_list = []

    for i in range(0, len(a), n):
        temp_list.append(list(a[i:(i+n)]))

    return temp_list

print(chunked(a,n))
