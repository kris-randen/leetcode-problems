import math
from collections import defaultdict
from typing import List


class IndexPQ:
    def __init__(self, keys):
        self.n = len(keys)
        self.keys = [-1] + keys
        self.pq = [-1] + [_ + 1 for _ in range(self.n)]
        self.qp = [-1] + [_ + 1 for _ in range(self.n)]
        self.N = None
        self.heapify()

    def size(self): return self.n if not self.N else self.N

    def empty(self): return self.size() == 0

    def key(self, i): return self.keys[self.pq[i]]

    def order(self, i, j):
        return i if self.key(i) < self.key(j) else j

    def pref(self, i, j):
        if not i: return j
        if not j: return i
        return self.order(i, j)

    def up(self, i): return i // 2

    def lt(self, i): return 2 * i

    def rt(self, i): return 2 * i + 1

    def is_legit(self, i): return i and 1 <= i <= self.size()

    def legit(self, i):
        return i if self.is_legit(i) else None

    def parent(self, c): return self.legit(self.up(c))

    def left(self, p): return self.legit(self.lt(p))

    def right(self, p): return self.legit(self.rt(p))

    def child(self, p): return self.pref(self.left(p), self.right(p))

    def bal_up(self, c):
        p = self.parent(c)
        if not p: return True
        return self.pref(p, c) == p

    def bal_down(self, p):
        return self.pref(self.child(p), p) == p

    def unbal_parent(self, c):
        return None if self.bal_up(c) else self.parent(c)

    def unbal_child(self, p):
        return None if self.bal_down(p) else self.child(p)

    def swap(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]] = i; self.qp[self.pq[j]] = j

    def lift(self, c):
        p = self.unbal_parent(c)
        if not p: return None
        self.swap(p, c); return p

    def drop(self, p):
        c = self.unbal_child(p)
        if not c: return None
        self.swap(p, c); return c

    def swim(self, c):
        while not self.bal_up(c): c = self.lift(c)

    def sink(self, p):
        while not self.bal_down(p): p = self.drop(p)

    def heapify(self):
        # print(f'self.n = {self.n}')
        for c in reversed(range(1, self.size() + 1)):
            # print(f'heapify sinking c = {c}')
            self.sink(c)

    def top(self):
        return self.keys[self.pq[1]]

    def pop(self):
        m = self.pq[1]
        top = self.keys[m]; self.swap(1, self.n)
        self.pq[self.n] = -1; self.qp[m] = self.n
        self.keys[m] = None
        self.n -= 1; self.sink(1)
        print(f'keys = {self.keys}')
        return top

    def change(self, i, key):
        self.keys[i] = key
        self.swim(self.qp[i])
        self.sink(self.qp[i])

    def sort(self):
        self.N = self.size()
        while self.N > 1:
            self.swap(1, self.N)
            self.N -= 1
            self.sink(1)
        res = self.pq.copy()
        self.N = None
        self.heapify()
        return res

class Edge:
    def __init__(self, u, v, wt):
        self.beg = u
        self.end = v
        self.wt = wt

class Wegraph:
    def __init__(self, V, es, directed=False):
        self.V = V
        self.directed = directed
        self.adj = defaultdict(set)
        self.adds(es)

    def add(self, e):
        self.adj[e.beg].add(e)
        if not self.directed: self.adj[e.end].add(e)

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
        self.dict[key], index = value, -1
        if key in self.qp:
            index = self.qp[key]
        else:
            self.pq.append(key); index = self.size()
        self.swim(index); self.sink(index)

    def top_key(self): return self.pq[1]

    def top_val(self): return self.dict[self.top_key()]

    def pop_key(self):
        self.swap(1, self.size())
        top = self.pq.pop()
        self.sink(1)
        self.qp.pop(top)
        self.dict.pop(top)
        return top

    def pop_val(self):
        top_val = self.dict[self.top_key()]
        self.pop_key()
        return top_val


class DijkstraB:
    def __init__(self, g, s):
        self.g = g; self.V = self.g.V
        self.dist_to = [float('inf')] * self.V
        self.pq = IndexPQ(self.dist_to)
        self.edge_to = [None for _ in range(self.V)]

        self.dist_to[s] = 0; self.pq.change(s, 0)

        while not self.pq.empty():
            v = self.pq.pop()
            for e in self.g.adj[v]:
                self.relax(e)

    def relax(self, e):
        u, v, wt = e.beg, e.end, e.wt
        dist = self.dist_to[u] + wt
        if self.dist_to[v] < dist:
            self.dist_to[v] = dist
            self.edge_to[v] = e
            self.pq.change(v, dist)


class Dijkstra:
    def __init__(self, g, s):
        self.g = g; self.dist_to = [float('inf')] * self.g.V
        self.dist_to[s] = 0; self.edge_to = [-1] * self.g.V
        self.pq = HeapDict(); self.pq[s] = self.dist_to[s]

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
        return -math.exp(dijk.dist_to[t])


if __name__ == '__main__':
    # v = [23, 0, 7, 5, 2, 11, 1]
    # pq = IndexPQ(v)
    # print(f'keys = {pq.keys}')
    # print(f'pq.. = {pq.pq}')
    # print(f'qp.. = {pq.qp}')
    # s = pq.sort()
    # print(f'sort = {s}')
    # print(f'pq.. = {pq.pq}')
    # print(f'pop = {pq.pop()}')
    # print(f'pop = {pq.pop()}')
    # print(f'pop = {pq.pop()}')
    # print(f'pq = {pq.pq}')
    # pq.change(3, -1)
    # print(f'pq = {pq.pq}')
    # print(list(range(10, 1, -1)))
    vs = [23, 0, 7, 5, 2, 11, 1]
    pq = HeapDict()
    for i, v in enumerate(vs): pq[i] = v
    print(pq.dict)
    print(pq.pq)



