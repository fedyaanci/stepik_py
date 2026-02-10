n = int(input())

m_list = [[] for _ in range(n)]

for i in range(n):
    m_list[i] = list(map(int, input().split()))

max_elem = None

for i in range(n):
    for j in range(n):
        if i >= n - 1 - j:  
            if max_elem is None or m_list[i][j] > max_elem:
                max_elem = m_list[i][j]

if max_elem is None:
    print("No elements below the anti-diagonal")
else:
    print(max_elem)