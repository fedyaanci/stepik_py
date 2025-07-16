n = int(input())

dict = {}

for i in range(1, n+1):
    dict[i] = input()
    
def search_anton(dict):
    anton_list = ['a','n','t','o','n']
    index = 0
    ill_fridge = set()
    flag = True
    for i in range(1, n+1):
        index = 0
        for j in range(len(dict[i])):
            if anton_list[index] == dict[i][j]:
                index +=1
                if index == len(anton_list):
                    ill_fridge.add(i)
                    break
        
    return ill_fridge

infected = search_anton(dict)
print(' '.join(map(str, sorted(infected)))) if infected else None