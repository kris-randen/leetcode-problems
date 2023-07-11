from collections import defaultdict

class Graph:
    def __init__(self, V, es, directed=True):
        self.V = V
        self.directed = directed
        self.adj = defaultdict(set)
        self.adds(es)
        self.reachable = [[(u == v or v in self.adj[u]) for v in range(self.V)] for u in range(self.V)]
        print(f'g = {self.adj}')
        for l in self.reachable:
            print(l)
        self.closure()
        print(f'after closure')
        for l in self.reachable:
            print(l)

    def add(self, e):
        u, v = e; self.adj[u].add(v)
        if not self.directed: self.adj[v].add(u)

    def adds(self, es):
        for e in es: self.add(e)

    def closure(self):
        for k in range(self.V):
            for u in range(self.V):
                for v in range(self.V):
                    self.reachable[u][v] = self.reachable[u][v] or \
                    (self.reachable[u][k] and self.reachable[k][v])

    def queries(self, qs):
        return list(map(lambda q: self.reachable[q[0]][q[1]], qs))

if __name__ == '__main__':
    n = 5
    ps = [[4, 3], [4, 1], [4, 0], [3, 2], [3, 1], [3, 0], [2, 1], [1, 0]]
    qs = [[1, 4], [4, 2], [0, 1], [4, 0], [0, 2], [1, 3], [0, 1]]
    g = Graph(n, ps)
    print(g.queries(qs))
