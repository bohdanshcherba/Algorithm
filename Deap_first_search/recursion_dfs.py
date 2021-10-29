from collections import defaultdict


class Graph:

    def __init__(self):

        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):

        visited.add(v)
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    def dfs(self, v):

        visited = set()

        self.dfs_util(v, visited)


g = Graph()

g.add_edge(3, 0)
g.add_edge(3, 10)
g.add_edge(0, 10)
g.add_edge(7, 9)
g.add_edge(11, 10)
g.add_edge(11, 5)
g.add_edge(8, 5)
g.add_edge(8, 4)
g.add_edge(5, 0)
g.add_edge(7, 10)
g.add_edge(5, 4)
g.add_edge(6, 10)
g.add_edge(8, 6)
g.add_edge(4, 11)
g.add_edge(10, 5)
g.add_edge(8, 1)
g.add_edge(6, 11)
g.add_edge(6, 1)
g.add_edge(9, 1)

g.dfs(3)
