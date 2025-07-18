input = input()
def to_form(input):
    letters='abcdefgh'
    x = ''
    for i in range(len(letters)):
        if letters[i]==input[0]:
            x=i
    if x == '':
        exit()
    return str(x)+str(input[1]) 
form_str = to_form(input)
y = int(form_str[0])
x = 8 - int(form_str[1]) 

table = [ ['.' for i in range(8)] for j in range(8) ]
table[x][y] = 'N'

for i in range(8):
    for j in range(8):
        if abs((i - x) * (j - y)) == 2:
            table[i][j] = '*'

for i in table:
    for j in i:
        print(j, end=' ')
    print()
