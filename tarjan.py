from collections import defaultdict


class Graph:
    def __init__(self, number_of_V):
        self.vertexes = defaultdict(list)
        self.number_of_V = number_of_V

        self.index = 0
        self.indexes = [-1] * self.number_of_V
        self.low_index = [-1] * self.number_of_V
        self.on_stack = [False] * self.number_of_V
        self.stack = []

        self.scc = list()

    def add_vertex(self, V, edge_to):
        self.vertexes[V].append(edge_to)

    def dfs(self, at):
        self.stack.append(at)
        self.on_stack[at] = True
        self.index += 1
        self.indexes[at] = self.index
        self.low_index[at] = self.index

        for to in self.vertexes[at]:
            if self.indexes[to] == -1:
                self.dfs(to)
                self.low_index[at] = min(self.low_index[at], self.low_index[to])

            elif self.on_stack[to]:
                self.low_index[at] = min(self.low_index[at], self.low_index[to])

        node = -1

        if self.indexes[at] == self.low_index[at]:
            arr = []
            while node != at:
                node = self.stack.pop()

                arr.append(node)
                self.on_stack[node] = False

            self.scc.append(arr)

    def tarjan(self):
        for i in range(self.number_of_V):
            if self.indexes[i] == -1:
                self.dfs(i)

        return self.scc


if __name__ == '__main__':
    # g1 = Graph(5)
    # g1.add_vertex(1, 0)
    # g1.add_vertex(0, 2)
    # g1.add_vertex(2, 1)
    # g1.add_vertex(0, 3)
    # g1.add_vertex(3, 4)
    #
    # print(g1.vertexes)
    # print(g1.tarjan())

    g2 = Graph(11)
    g2.add_vertex(0, 2)
    g2.add_vertex(2, 4)
    g2.add_vertex(2, 10)
    g2.add_vertex(4, 8)
    g2.add_vertex(4, 6)
    g2.add_vertex(4, 0)
    g2.add_vertex(6, 8)
    g2.add_vertex(8, 7)
    g2.add_vertex(8, 1)
    g2.add_vertex(8, 3)
    g2.add_vertex(1, 3)
    g2.add_vertex(1, 9)
    g2.add_vertex(3, 6)
    g2.add_vertex(7, 5)
    g2.add_vertex(10, 5)
    g2.add_vertex(10, 7)
    g2.add_vertex(9, 7)
    g2.add_vertex(5, 9)

    print(g2.vertexes)
    print(g2.tarjan())
