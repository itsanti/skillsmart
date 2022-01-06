class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        return None

    def size(self):
        return len(self.queue)

class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size  # максимальное количество вершин
        self.m_adjacency = [[0] * size for _ in range(size)]  # матрица смежности 0 и 1
        self.vertex = [None] * size  # список вершин. по индексу поиск вершины и связи с другими по матрице

    def AddVertex(self, v):
        ix = -1
        if None in self.vertex:
            ix = self.vertex.index(None)
            self.vertex[ix] = Vertex(v)
        return ix

    # здесь и далее, параметры v -- индекс вершины в списке  vertex

    def RemoveVertex(self, v):
        # ваш код удаления вершины со всеми её рёбрами
        if v >= self.max_vertex:
            return False
        for v2 in range(self.max_vertex):
            if self.IsEdge(v, v2):
                self.RemoveEdge(v, v2)
        self.vertex[v] = None
        return True

    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        if all([v1 < self.max_vertex, v2 < self.max_vertex]):
            return self.m_adjacency[v1][v2] == 1
        return False

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        if all([v1 < self.max_vertex, v2 < self.max_vertex]):
            self.m_adjacency[v1][v2], self.m_adjacency[v2][v1] = 1, 1
            return True
        return False

    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        if all([v1 < self.max_vertex, v2 < self.max_vertex]):
            self.m_adjacency[v1][v2], self.m_adjacency[v2][v1] = 0, 0
            return True
        return False

    def DepthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        if any([VFrom >= len(self.vertex), VTo >= len(self.vertex), VFrom < 0, VTo < 0]):
            return []
        if any([self.vertex[VFrom] is None, self.vertex[VTo] is None]):
            return []
        if VFrom == VTo:
            return [self.vertex[VFrom]]

        for v in self.vertex:
            if v is not None:
                v.Hit = False

        path = []

        current_vertex = VFrom

        while True:
            self.vertex[current_vertex].Hit = True
            path.append(self.vertex[current_vertex])

            if self.IsEdge(current_vertex, VTo):
                path.append(self.vertex[VTo])
                return path

            for v in range(self.max_vertex):
                if self.IsEdge(current_vertex, v) and not self.vertex[v].Hit:
                    current_vertex = v
                    break
            else:
                path.pop()
                if len(path) == 0:
                    return []
                else:
                    current_vertex = self.vertex.index(path.pop())

    def BreadthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        if any([VFrom >= len(self.vertex), VTo >= len(self.vertex), VFrom < 0, VTo < 0]):
            return []
        if any([self.vertex[VFrom] is None, self.vertex[VTo] is None]):
            return []
        if VFrom == VTo:
            return [self.vertex[VFrom]]

        for v in self.vertex:
            if v is not None:
                v.Hit = False

        queue = Queue()
        queue.enqueue(VFrom)

        path = {v: [] for v in range(self.max_vertex)}

        while queue.size() > 0:
            current_vertex = queue.dequeue()
            self.vertex[current_vertex].Hit = True
            for v in range(self.max_vertex):
                if self.IsEdge(current_vertex, v) and not self.vertex[v].Hit:
                    path[v].append(path[current_vertex] + [current_vertex])
                    if v == VTo:
                        path[v].append(VTo)
                        return [self.vertex[vertex] for vertex in SimpleGraph.getPath(path[VTo])]
                    queue.enqueue(v)
        return []

    @staticmethod
    def getPath(path):
        result = []
        while True:
            result.append(path.pop())
            if len(path) == 0:
                break
            path = min(path, key=len)
        return result[::-1]
