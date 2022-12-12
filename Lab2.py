class Graph:
    def __init__(self, A, C, vertix):
        self.A = A
        self.C = C
        self.vertix = vertix

    def FIRST(self, v):
        for i in range(len(self.A)):
            if self.A[self.vertix.index(v)][i]:
                return i
        return -1

    def NEXT(self, v, i):
        for j in range(i+1, len(self.A)):
            if self.A[self.vertix.index(v)][j]:
                return j
        return -1

    def VERTEX(self, v, i):
        j = self.FIRST(v)
        temp = []
        while j != -1:
            temp.append(self.vertix[j])
            j = self.NEXT(v, j)
        if i <= len(temp):
            return self.vertix[self.vertix.index(temp[i])]

    def ADD_V(self, name):
        self.vertix.append(name)
        for j in range(len(self.A)):
            self.A[j].append(0)
            self.C[j].append(0)
        self.A.append([0 for j in range(self.vertix.index(name)+1)])
        self.C.append([0 for j in range(self.vertix.index(name)+1)])

    def ADD_Е(self, v, w, c):
        self.A[self.vertix.index(v)][self.vertix.index(w)] = 1

        self.C[self.vertix.index(v)][self.vertix.index(w)] = c

    def DEL_V(self, name):
        self.A.pop(self.vertix.index(name))
        self.C.pop(self.vertix.index(name))
        for j in range(len(self.A)):
            self.A[j].pop(self.vertix.index(name))
            self.C[j].pop(self.vertix.index(name))
        self.vertix.remove(name)

    def DEL_Е(self, v, w):
        self.A[self.vertix.index(v)][self.vertix.index(w)] = 0

    def EDIT_V(self, name, new_name):
        self.vertix[self.vertix.index(name)] = new_name

    def EDIT_Е(self, v, w, c):
        if (self.C[self.vertix.index(v)][self.vertix.index(w)] != 0):
            self.C[self.vertix.index(v)][self.vertix.index(w)] = c


def min_cut(gr):
    temp = gr.A
    temp_count = []
    first = 0
    a = gr.C[first][gr.FIRST(gr.vertix[first])]
    temp[first][gr.FIRST(gr.vertix[first])] = 0
    b = gr.C[first][gr.FIRST(gr.vertix[first])]
    temp_count.append([a, b])
    temp_count.append([gr.C[1][gr.FIRST(gr.vertix[1])], b])
    k2 = 1
    while gr.C[k2][gr.FIRST(gr.vertix[k2])] != 0:
        temp_count1 = []
        a1 = gr.C[k2][gr.FIRST(gr.vertix[k2])]
        k = 2
        while k != -1:
            if sum(temp[k]) > 1:
                while sum(temp[k]) > 1:
                    if k2 < len(gr.vertix) - 2:
                        temp_count1.append(gr.C[k][gr.FIRST(gr.vertix[k])])
                    temp[k][gr.FIRST(gr.vertix[k])] = 0
                    temp_count1.append(gr.C[k][gr.FIRST(gr.vertix[k])])
                    if k < len(gr.vertix) - 1 and k2 >= 1:
                        temp_count1.append(sum(gr.C[k2]))
                    else:
                        temp_count1.append(a1)
            else:
                temp_count1.append(gr.C[k][gr.FIRST(gr.vertix[k])])
                temp_count1.append(a1)
            temp_count.append(temp_count1)

            if k2 < len(gr.vertix) - 2:
                temp_count1 = temp_count1[:1]
            else:
                temp_count1 = []
            k = gr.NEXT(gr.vertix[k], gr.FIRST(gr.vertix[k-1]))
        # print(temp_count)
        k2 = gr.NEXT(gr.vertix[k2], gr.FIRST(gr.vertix[k2-1]))

    temp_sum = []
    for i in range(len(temp_count)):
        temp_sum.append(sum(temp_count[i]))
    return min(temp_sum)


vertix = ['O', 'A', 'B', 'C', 'D', 'T']
A = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0]
]  # матрица смежности
C = [
    [0, 8, 3, 0, 0, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 0, 4, 2, 0],
    [0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0]
]  # матрица цен

vertix2 = ['O', 'A', 'B', 'C', 'D', 'T']
A2 = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0]
]  # матрица смежности
C2 = [
    [0, 9, 3, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 5, 8, 0],
    [0, 0, 0, 0, 2, 6],
    [0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0]
]  # матрица цен

graph = Graph(A, C, vertix)
graph2 = Graph(A2, C2, vertix2)

print("Индекс первой смежной вершины О: ", graph.FIRST('O'))
print("Индекс смежной вершины О после 0: ", graph.NEXT('O', 0))
print("Вершина с индексом 0 из множества вершин, смежных с А: ", graph.VERTEX('A', 0))

print("--------------------------------------------------------")

print("До добавления вершины и дуги:")

print(vertix)

print("\nМатрица смежности: ")
for line in A:
    print(*line)
print("\nМатрица цен: ")
for line in C:
    print(*line)

graph.ADD_V('G')

graph.ADD_Е('T', 'G', 10)

print("\nПосле добавления вершины и дуги:")

print(vertix)

print("\nМатрица смежности: ")
for line in A:
    print(*line)
print("\nМатрица цен: ")
for line in C:
    print(*line)

print("\nПосле удаления вершины и дуги:")

graph.DEL_Е('T', 'G')
graph.DEL_V('G')

print("\nМатрица смежности: ")
for line in A:
    print(*line)
print("\nМатрица цен: ")
for line in C:
    print(*line)

print("\nПосле изменения вершины:")

graph.EDIT_V('T', 'F')

print(vertix, "\nизменили T на F")

print("\nПосле изменения веса дуги:")

graph.EDIT_Е('O', 'A', 9)

print("\nМатрица цен: ")
for line in C:
    print(*line)

print("\nизменили O->A c 8 на 9")

print("--------------------------------------------------------")

print("1 Граф")
print(vertix)
print("\nМатрица смежности: ")
for line in A:
    print(*line)

print()
print("\nМатрица цен: ")
for line in C:
    print(*line)


print("\nМинимальный разрез = ", min_cut(graph))

print("2 Граф")
print(vertix2)
print("\nМатрица смежности: ")
for line in A2:
    print(*line)

print()
print("\nМатрица цен: ")
for line in C2:
    print(*line)


print("\nМинимальный разрез = ", min_cut(graph2))