from collections import defaultdict
str_1 = input()
str_2 = input()

dict_from_str1 = defaultdict(int)
dict_from_str2 = defaultdict(int)

for word in str_1:
    if word.strip('/,.!@#$%^&*()-" ') != '':
        dict_from_str1[word.strip('/,.!@#$%^&*()-" ').lower()] += 1

for word in str_2:
    if word.strip('/,.!@#$%^&*()-" ') != '':
        dict_from_str2[word.strip('/,.!@#$%^&*()-" ').lower()] += 1

print(dict_from_str1)
print(dict_from_str2)

if dict_from_str2 == dict_from_str1:
    print('YES')
else:
    print('NO')