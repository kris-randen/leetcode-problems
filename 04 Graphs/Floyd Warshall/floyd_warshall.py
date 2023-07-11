from collections import defaultdict

class Graph:
    def __init__(self, V, es):
        self.V = V
        self.adj = defaultdict(defaultdict)
        self.adds(es)
        self.dist = [[float('inf') for _ in range(self.V)] for _ in range(self.V)]
        for u in range(self.V):
            for v in range(self.V):
                self.dist[u][v] = self.adj[u][v] if u in self.adj[v] else 0

    def add(self, ew):
        u, v, w = ew; self.adj[u][v] = w

    def adds(self, ews):
        for ew in ews: self.add(ew)

    def floyd_warshall(self):
        for k in range(self.V):
            for u in range(self.V):
                for v in range(self.V):
                    self.dist[u][v] = min(
                        self.dist[u][v], self.dist[u][k] + self.dist[k][v]
                    )


