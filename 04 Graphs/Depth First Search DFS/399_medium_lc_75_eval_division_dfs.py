"""

399. Evaluate Division
Medium
8.3K
744
Companies
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.



Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

"""


"""

Python Depth-First Search (DFS) and Union-Find Beats 95%
kris-randen
237
3
an hour ago
Python3
Intuition
Depth-First Search (DFS) and Union-Find
We use union-find with path compression to store values already computed using DFS.

Approach
We can use bare DFS but that will lead to recomputing many paths again and again. So a more efficient way is to cache this information. We can do that using a map / dict but instead a better more elegant way is to use a special edge-weighted union-find graph datastructure.

This graph a disjoint-set of all symbols added to the graph through the equations. Every time we insert / add an equation we make the numerator the parent of the denominator by assigning the num as the id for denom.

A natural root emerges just like in union-find. Every time we are given a query we check if the two symbols in the query belong to the same disjoint-set. If not we return -1.

Complexity
Time complexity:
O(m * alpha(n)) where m is the number of operations aka equations + queries. alpha(n) is the inverse Ackerman function.

Note that eventually if the number of queries far outweighs the number of equations we'll reach O(m) eventually as the fully path compressed union-find graph will be able to return every query [a, b] by looking the common root r and the returning (a / r) * (r / b).

Space complexity:
O(n ^ 2) as we could end up storing almost every pair of symbols in the edge-weighted graph. This could be futher simplified to O(n) by recognizing that after full path compression all we need is a tree / star where each symbol is connedted to the common root.

"""

from collections import defaultdict

from typing import List


class Graph:
    def __init__(self, sbs):
        self.g = {sb: {sb: 1.0} for sb in sbs}
        self.id = {sb: sb for sb in sbs}
        self.sz = {sb: 1 for sb in sbs}

    def parent(self, c):
        return self.id[c]

    def assign(self, c, p):
        self.id[c] = p

    def is_root(self, p):
        return p == self.parent(p)

    def size(self, p):
        return self.sz[p]

    def order(self, p, q):
        l, s = self.root(p), self.root(q)
        return [(p, l), (q, s)] if self.size(l) > self.size(s) else [(q, s), (p, l)]

    def path(self, c):
        path = [c]
        while not self.is_root(c):
            c = self.parent(c)
            path.append(c)
        return path

    def compress(self, c):
        path = self.path(c)
        n = len(path)
        root = path[-1]
        product = 1
        for i in reversed(range(1, n)):
            v = path[i]
            w = path[i - 1]
            self.g[root][v] = product
            self.g[v][root] = 1 / product
            self.search(v, w)
            product = product * self.g[v][w]
            self.assign(v, root)
            self.assign(w, root)
        return root

    def root(self, c):
        return self.compress(c)

    def iso_root(self, p, q):
        return self.root(p) == self.root(q)

    def find(self, p, q):
        if p not in self.g or q not in self.g: return - 1
        if not self.iso_root(p, q): return -1
        if q in self.g[p]: return self.g[p][q]
        r, s = self.root(p), self.root(q)
        l, m = self.g[p][r], self.g[s][q]
        return l * m

    def search(self, v, w):
        if w in self.g[v] and v in self.g[w]: return
        if w in self.g[v] and v not in self.g[w]:
            self.g[w][v] = 1 / self.g[v][w];
            return
        if v in self.g[w] and w not in self.g[v]:
            self.g[v][w] = 1 / self.g[w][v];
            return
        visited = defaultdict(int)

        def dfs(i, w, prod):
            if i in visited: return
            visited[i] = prod
            if i == w: return
            for u in self.g[i]:
                if u != i:
                    prod = visited[i] * self.g[i][u]
                    dfs(u, w, prod)

        dfs(v, w, 1)
        prod = visited[w]
        self.g[v][w] = prod
        self.g[w][v] = 1 / prod

    def add_edge(self, v, w, val):
        self.g[v][w] = val
        self.g[w][v] = 1 / val
        if self.iso_root(v, w): return
        p, q = self.root(v), self.root(w)
        if self.size(p) >= self.size(q):
            self.assign(q, p)
            self.sz[p] += self.sz[q]
        else:
            self.assign(p, q)
            self.sz[q] += self.sz[p]
        self.g[p][q] = self.g[p][v] * val * self.g[w][q]
        self.g[q][p] = 1 / self.g[p][q]

    def add_edges(self, eqs, vals):
        for i in range(len(eqs)):
            v, w = eqs[i]
            self.add_edge(v, w, vals[i])

    def queries(self, qs):
        res = []
        for q in qs:
            v, w = q
            res.append(self.find(v, w))
        return res


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        sbs = set()
        for eq in equations:
            sbs.add(eq[0]);
            sbs.add(eq[1])
        g = Graph(sbs)
        g.add_edges(equations, values)
        return g.queries(queries)