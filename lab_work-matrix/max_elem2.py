n = int(input())

m_list=[[] for _ in range(n)]

for i in range(n):
        m_list[i].append(list(map(int, (input().split()))))

max_elem = m_list[n-1][n-1]

for i in range(n):
    for j in range(n):
        if (i>n-1-j):
            if m_list[i][j]> max_elem:
                 max_elem = m_list[i][j]                
print(m_list) 