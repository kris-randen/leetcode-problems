class Graph:
    def __init__(self, V, es, directed=False):
        self.V = V
        self.directed = directed
        self.adj = {v: {v: 0} for v in range(self.V)}
        self.adds(es)
        self.dist = [[0 for _ in range(self.V)] for _ in range(self.V)]
        for u in range(self.V):
            for v in range(self.V):
                self.dist[u][v] = self.adj[u][v] if v in self.adj[u] else (0 if u == v else float('inf'))
        self.floyd_warshall()

    def add(self, ew):
        u, v, w = ew; self.adj[u][v] = w
        if not self.directed: self.adj[v][u] = w

    def adds(self, ews):
        for ew in ews: self.add(ew)

    def floyd_warshall(self):
        for k in range(self.V):
            for u in range(self.V):
                for v in range(self.V):
                    self.dist[u][v] = min(
                        self.dist[u][v], self.dist[u][k] + self.dist[k][v]
                    )


