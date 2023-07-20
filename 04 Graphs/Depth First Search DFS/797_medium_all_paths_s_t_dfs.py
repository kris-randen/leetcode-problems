"""

797. All Paths From Source to Target
Medium
6.7K
137
Companies
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).



Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

"""

from collections import defaultdict
from typing import List


class Graph:
    def __init__(self, V, es=None, directed=True):
        self.V = V;
        self.directed = directed
        self.adj = defaultdict(list)
        self.es = es if es else []
        for u, v in self.es:
            self.add(u, v)

    def add(self, u, v):
        self.adj[u].append(v)
        if not self.directed: self.adj[v].append(u)


"""
1. DFS
"""


class DFS:
    def __init__(self, g):
        self.g = g
        self.visited = [0] * self.g.V

    def clear(self):
        self.visited = [0] * self.g.V

    def paths(self, s, t):
        all_ps = []

        def dfs(u, w, ps):
            if self.visited[u] and u != w: return
            if u == w: ps.append(u); all_ps.append(ps); return
            self.visited[u] = 1
            for v in self.g.adj[u]:
                dfs(v, w, ps + [u])
            self.visited[u] = 0

        self.clear()
        dfs(s, t, [])
        return all_ps


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        V = len(graph);
        g = Graph(V)
        for v, ws in enumerate(graph):
            g.adj[v] = ws
        df = DFS(g)
        return df.paths(0, V - 1)