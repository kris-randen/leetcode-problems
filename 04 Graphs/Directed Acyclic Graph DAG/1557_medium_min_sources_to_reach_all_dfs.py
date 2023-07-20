"""

1557. Minimum Number of Vertices to Reach All Nodes
Medium
3.4K
114
Companies
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.



Example 1:



Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].
Example 2:



Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]
Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.

"""

from collections import defaultdict

class Graph:
    def __init__(self, V, es=None, directed=True):
        self.V = V; self.es = es if es else []
        self.badj = defaultdict(set)
        self.directed = directed
        for u, v in self.es:
            self.add(v, u)

    def add(self, u, v):
        self.badj[u].add(v)
        if not self.directed: self.badj[v].add(u)

class DFS:
    def __init__(self, g):
        self.g = g; self.visited = [0] * self.g.V

    def sources(self):
        srcs = set()

        def dfs(u):
            if self.visited[u]: return
            self.visited[u] = 1
            if not self.g.badj[u]:
                srcs.add(u)
                return
            for v in self.g.badj[u]:
                dfs(v)

        for v in range(self.g.V): dfs(v)
        return srcs
