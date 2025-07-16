a =  list(map(int, input().split()))

def count_unique(a):
    list_unique = []
    for i in a:
        if i not in list_unique:
            list_unique.append(i)
    return len(list_unique)

def count_unique2(a):
    uniq=set(a)
    return len(uniq)

print(count_unique2(a))


