m_dict = {}

for i in range(int(input())):
    pair_word = input().split()
    m_dict[pair_word[0]], m_dict[pair_word[1]] = pair_word[1], pair_word[0]

print(m_dict[input()])
