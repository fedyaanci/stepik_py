num_list = list(map(int, input().split()))
counter = 0

for i in range(len(num_list)-1):  # Измененный диапазон
    if num_list[i] < num_list[i+1]:
        counter += 1

print(counter)