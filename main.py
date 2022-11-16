import random

class Graph:  # Граф представлен списком узлов и содержим в каждом узле.

    def __int__(self):
        self.node = []

    def makeGraph(self, sizeGraph: int, bound: list, content: list = ['0']):
        if len(content) <= sizeGraph:
            self.content = content + [0] * (sizeGraph - len(content))
        self.node = [0] * sizeGraph
        for i in range(sizeGraph):
            self.node[i] = [bound[i], self.content[i]]


def DFS(graph: Graph, content: str, location: int = 0, way: list = []):
    global counterNode  # Список всех посещённых вершин
    global findX  # Используется для возврата положения искомого узла.
    global maxWay  # Длина пути, размер требуемых для поиска данных.
    waygo = way + [location]  # будущий и текущие пути.
    if location not in counterNode:  # записываем
        counterNode += [location]
    if len(waygo) > len(maxWay):
        maxWay = waygo
    if graph.node[location][1] == content:  # Проверяем содержимое узла в котором мы находимся.
        findX = (location)

    else:
        if graph.node[location][0] is not []:  # Если есть пути, то по всем путям проводим рекурсию.
            for i in graph.node[location][0]:
                if i not in waygo:
                    DFS(graph, content, i, waygo)
                    if findX != -1:  # Находим ответ и выходим.
                        break
    return (findX)


def BFS(graph: Graph, content: str, location: list = []):
    global counterNode1  # Список всех посещённых вершин
    global findX  # Используется для возврата положения искомого узла.
    global maxWay  # Длина пути, размер требуемых для поиска данных.
    locGo = []  # куда идём
    for j in location:
        if j not in counterNode1:
            counterNode1 += [j]
    if len(counterNode1) > len(maxWay):
        maxWay += counterNode1
    if location != []:
        for i in location:
            if findX != -1:  # Находим ответ и выходим.
                break
            if graph.node[i][1] == content:  # Проверяем содержимое узла в котором мы находимся.
                findX = i
            else:
                for j in graph.node[i][0]:
                    if j not in counterNode1:
                        locGo += [j]
                        counterNode1 += [j]
        BFS(graph, content, locGo)
    return(findX)


if __name__ == '__main__':
    edge = 4
    bound = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
             []]  # Связи между узлами представлены в виде списка списков
    content = [0] * 16  # Изначально
    g = Graph()
    g1 = Graph()
    random.seed(version=2)
    elements = ['#', '#', '#', 'x', 'x', 'x', 'A', 'E'] + 8 * ['0']
    for i in range(edge):
        for j in range(edge):
            content[i * 4 + j] = elements.pop(
                random.randint(0, len(elements) - 1))  # Случайно распределяем содержимое по графу.
            if content[i * 4 + j] == 'A':
                locA = i * 4 + j
    deadpool = []  # Список непроходимых участков.
    for i in range(edge):  # Представляем в виде полностью связанной сетки 4х4.
        for j in range(edge):
            if ((i + 1) * 4 + j) >= 0 and ((i + 1) * 4 + j) <= 15 and (i + 1) <= 3:
                bound[i * 4 + j] += [(i + 1) * 4 + j]
            if ((i - 1) * 4 + j) >= 0 and ((i - 1) * 4 + j) <= 15 and (i - 1) >= 0:
                bound[i * 4 + j] += [(i - 1) * 4 + j]
            if (i * 4 + j + 1) >= 0 and (i * 4 + j + 1) <= 15 and (j + 1) <= 3:
                bound[i * 4 + j] += [i * 4 + j + 1]
            if (i * 4 + j - 1) >= 0 and (i * 4 + j - 1) <= 15 and (j - 1) >= 0:
                bound[i * 4 + j] += [i * 4 + j - 1]
            if content[i * 4 + j] == '#':  # Удаляем связи у непроходимых участков.
                deadpool += [i * 4 + j]
                bound[i * 4 + j] = []
    for i in range(edge):  # Удаляем связи с непроходимыми участками
        for j in range(edge):
            for y in deadpool:
                try:
                    bound[i * 4 + j].remove(y)
                except:
                    pass
    locA1 = locA  #Для повторного вызова BFS
    findX = -1  # глобальная переменная для поиска.
    maxWay = [0]  # Максимум пути в памяти для каждого поиска.
    way = [locA]  # Весь путь агента.
    counterNode = []  # Определяем список всех посещённых вершин
    for i in range(edge):
        print('|', content[i * 4], content[i * 4 + 1], content[i * 4 + 2], content[i * 4 + 3], '|')
    g.makeGraph(edge ** 2, bound, content)
    xCount = 3
    xFlag = 0
    while xCount > 0 and xFlag == 0:  # Поиск мест.
        placeX = DFS(g, 'x', locA)  # Ищем место, если место не нашли, пишем флаг и выходим из поиска
        if placeX == -1:
            xFlag = 1
        way += maxWay[1:len(maxWay)]  # Добавляем текущий путь в общий
        maxWay = []  # Обнуляем текущий путь
        g.node[placeX][1] = '0'  # Обнуляем место
        xCount -= 1
        locA = placeX
        findX = -1
    if xFlag == 1:
        print('У агента нет пути')
    else:
        placeE = DFS(g, 'E', placeX)
        way += maxWay[1:len(maxWay)]
        if placeE == -1:
            print('У агента нет пути')
        else:
            print("Путь агента DFS", way)
            print("Количество раскрытых вершин DFS ", len(counterNode))

    findX = -1  # глобальная переменная для поиска.
    way = [locA1]  # Весь путь агента.
    counterNode1 = []  # Определяем список всех посещённых вершин
    location = [locA1]
    g1.makeGraph(edge ** 2, bound, content)
    xCount = 3
    xFlag = 0
    while xCount > 0 and xFlag == 0:  # Поиск мест.
        placeX = BFS(g1, 'x', location)  # Ищем место, если место не нашли, пишем флаг и выходим из поиска
        if placeX == -1:
            xFlag = 1
        way += maxWay[1:len(maxWay)]  # Добавляем текущий путь в общий
        maxWay = []  # Обнуляем текущий путь
        g1.node[placeX][1] = '0'  # Обнуляем место
        xCount -= 1
        locA1 = placeX
        findX = -1
        counterNode1 = []
    if xFlag == 1:
        print('У агента нет пути')
    else:
        placeE = BFS(g1, 'E', [placeX])
        way += maxWay[1:len(maxWay)]
        if placeE == -1:
            print('У агента нет пути')
        else:
            way = list(set(way))
            print("Количество раскрытых вершин BFS ", len(way))
