import copy


class Graph:
    def __init__(self):
        self.vertexes = dict()

    def add_edge(self, v, w):
        if v in self.vertexes.keys():
            self.vertexes[v].append(w)
        else:
            self.vertexes[v] = [w]

    def dfs(self, start_vertex):
        accessible = copy.deepcopy(self.vertexes)
        active = list()

        key = start_vertex

        active.append(start_vertex)
        while True:

            if key not in accessible.keys() or not accessible[key]:
                active.pop()

                if not active:
                    return False
                else:
                    key = active[-1]
                    continue

            key = accessible[key].pop(0)
            if key == start_vertex:
                return active

            active.append(key)


def read_graph(file_name):
    graph = list()
    with open(file_name, 'r') as file:
        for l in file:
            l = l.strip().split()

            graph.append(list(l))
    return graph


def deap_first_search(file_name):
    graph_pairs = read_graph(file_name)
    edges = graph_pairs.pop(0)

    g = Graph()
    for i in graph_pairs:
        g.add_edge(int(i[0]), int(i[1]))

    for k in g.vertexes.keys():
        result = g.dfs(k)
        if result:
            return result
    return False


if __name__ == '__main__':
    print(deap_first_search('graph3.txt'))
