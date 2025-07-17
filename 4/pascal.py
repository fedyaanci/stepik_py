n = int(input())

def generate_pascal(n):
    
    if n ==0:
      return []
   
    triangle = [[1]]

    for i in range(1,n): # От 1 до n потому что первый элемент [0] мы сделали  triangle = [[1]]
        prev = triangle[-1] # предыдщую строку сохраняем для того чтобы посчитать текущую
        cur = [1] # всегда первый элемент новой строки убдет равен 1

        for j in range(1, i): # первый элемент доавблен уже он 1  --- для серединных значений
            cur.append(prev[j] + prev[j-1]) #добавялем новый элемент
      
        cur.append(1)

        triangle.append(cur)

    return triangle


triangle_pascal = generate_pascal(n)


for i in triangle_pascal:
    for j in i:
        print(j, end = ' ')
    print()