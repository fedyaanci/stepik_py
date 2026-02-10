"""input n - amount words in dict, 
    in every str word: opinion"""

n = int(input()) # amount words in dict
m_dict = {}
for i in range(n):
    word_opinion = input().split(sep=': ')
    m_dict[word_opinion[0]] = word_opinion[1]

m = int(input())# amount researching words
m_list = []
for i in range(m):
    m_list.append(input())

for elem in m_list:
    if elem in m_dict.keys():
        print(m_dict[elem])
    elif elem.capitalize() in m_dict.keys():
        print(m_dict[elem.capitalize()])
    else:
        print('Не найдено')