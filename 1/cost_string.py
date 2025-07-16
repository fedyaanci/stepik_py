input = input()

length = len(input)

print(str(length * 60 // 100) + ' р. ' + str(length * 60 % 100) + ' коп.')