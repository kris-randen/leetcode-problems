"""

1514. Path with Maximum Probability
Medium
2.9K
63
Companies
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.



Example 1:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
Example 2:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000
Example 3:



Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.

"""
import math
from collections import defaultdict
from typing import List

import heapdict

class Edge:
    def __init__(self, u, v, wt):
        self.beg = u
        self.end = v
        self.wt = wt

    def __str__(self):
        return f's = {self.beg}, t = {self.end}, wt = {self.wt}'

    def __repr__(self):
        return self.__str__()

class Wegraph:
    def __init__(self, V, es, directed=False):
        self.V = V
        self.directed = directed
        self.adj = defaultdict(set)
        self.adds(es)

    def add(self, e):
        self.adj[e.beg].add(e)
        if not self.directed: self.adj[e.end].add(Edge(e.end, e.beg, e.wt))

    def adds(self, es):
        for e in es: self.add(e)

class HeapDict:
    def __init__(self,order=None, dic=None):
        self.pq, self.qp, self.dict, self.N = [-1], {}, {}, None
        self.order = order if order else (lambda x, y: x if x < y else y)
        if dic: pass

    def size(self):
        return len(self.pq) - 1 if not self.N else self.N

    def is_empty(self): return self.size() == 0

    def __getitem__(self, key):
        return self.dict[key]

    def up(self, i): return i // 2

    def lt(self, i): return 2 * i

    def rt(self, i): return (2 * i) + 1

    def val(self, i): return self.dict[self.pq[i]]

    def ord(self, i, j):
        return i if self.order(self.val(i), self.val(j)) == self.val(i) else j

    def pref(self, i, j):
        if i and j: return self.ord(i, j)
        return i if not j else i

    def is_valid(self, i): return 1 <= i <= self.size()

    def valid(self, i):
        return i if self.is_valid(i) else None

    def left(self, p): return self.valid(self.lt(p))

    def right(self, p): return self.valid(self.rt(p))

    def child(self, p): return self.pref(self.left(p), self.right(p))

    def parent(self, c): return self.valid(self.up(c))

    def bal_up(self, c):
        p = self.parent(c)
        return True if not p else self.pref(p, c) == p

    def bal_down(self, p):
        return self.pref(self.child(p), p) == p

    def unbal_p(self, c):
        if not self.bal_up(c): return self.parent(c)

    def unbal_c(self, p):
        if not self.bal_down(p): return self.child(p)

    def swap(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]], self.qp[self.pq[j]] = i, j

    def lift(self, c):
        p = self.unbal_p(c)
        if p: self.swap(p, c)
        return p

    def drop(self, p):
        c = self.unbal_c(p)
        if c: self.swap(p, c)
        return c

    def swim(self, c):
        while c: c = self.lift(c)

    def sink(self, p):
        while p: p = self.drop(p)

    def heapify(self):
        for i in range(self.size(), 0, -1): self.sink(i)

    def sort(self):
        self.N = self.size()
        while self.N > 1:
            self.swap(1, self.N); self.N -= 1; self.sink(1)
        self.N = None
        ordered = [self.dict[self.pq[i]] for i in range(1, self.size() + 1)]; self.heapify()
        return ordered

    def __setitem__(self, key, value):
        if key in self.dict:
            index = self.qp[key]
        else:
            self.pq.append(key); index = self.size()
        self.dict[key] = value; self.qp[key] = index
        self.swim(index); self.sink(index)

    def top_key(self): return self.pq[1]

    def top_val(self): return self.dict[self.top_key()]

    def pop_key(self):
        self.swap(1, self.size())
        top = self.pq.pop()
        self.sink(1)
        self.qp.pop(top)
        if top in self.dict: self.dict.pop(top)
        return top

    def pop_val(self):
        top_val = self.dict[self.top_key()]
        self.pop_key()
        return top_val

class Dijkstra:
    def __init__(self, g, s):
        self.g = g; self.dist_to = [float('inf')] * self.g.V
        self.dist_to[s] = 0; self.edge_to = [-1] * self.g.V
        self.pq = HeapDict()
        for v in range(self.g.V):
            self.pq[v] = self.dist_to[v]

        while not self.pq.is_empty():
            v = self.pq.pop_key()
            for e in self.g.adj[v]:
                self.relax(e)

    def relax(self, e):
        u, v, wt = e.beg, e.end, e.wt
        du, dv = self.dist_to[u], self.dist_to[v]
        if dv > du + wt:
            self.dist_to[v] = du + wt
            self.edge_to[v] = e
            self.pq[v] = self.dist_to[v]

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], s: int,
                       t: int) -> float:
        es = []
        for i, edge in enumerate(edges):
            es.append(Edge(edge[0], edge[1], -math.log(succProb[i])))
        g = Wegraph(n, es)
        dijk = Dijkstra(g, s)
        return math.exp(-dijk.dist_to[t])
