"""

743. Network Delay Time
Medium
6.7K
336
Companies
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.



Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

"""

from collections import defaultdict
from heapq import *
from typing import List

class HeapDict:
    def __init__(self, order=None):
        self.pq, self.qp, self.dict, self.N = [-1], {}, {}, None
        self.order = order if order else (lambda x, y: x if x < y else y)

    def __getitem__(self, key): return self.dict[key]

    def __len__(self): return len(self.pq) - 1 if not self.N else self.N

    def is_valid(self, i): return 1 <= i <= len(self)

    def valid(self, i): return i if self.is_valid(i) else None

    def is_empty(self): return len(self) == 0

    def key(self, i): return self.pq[i]

    def val(self, i):
        return self.dict[self.key(i)]

    def item(self, i): return self.key(i), self.val(i)

    def ord(self, i, j):
        return i if self.order(self.val(i), self.val(j)) == self.val(i) else j

    def pref(self, i, j):
        if i and j: return self.ord(i, j)
        return i if not j else j

    def up(self, i): return i // 2

    def lt(self, i): return 2 * i

    def rt(self, i): return (2 * i) + 1

    def parent(self, c): return self.valid(self.up(c))

    def left(self, p): return self.valid(self.lt(p))

    def right(self, p): return self.valid(self.rt(p))

    def child(self, p): return self.pref(self.left(p), self.right(p))

    def bal_up(self, c):
        p = self.parent(c)
        if not p: return True
        return self.pref(p, c) == p

    def bal_dn(self, p):
        return self.pref(self.child(p), p) == p

    def unbal_p(self, c):
        return None if self.bal_up(c) else self.parent(c)

    def unbal_c(self, p):
        return None if self.bal_dn(p) else self.child(p)

    def swap(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]], self.qp[self.pq[j]] = i, j

    def lift(self, c):
        p = self.unbal_p(c)
        if not p: return None
        self.swap(p, c); return p

    def drop(self, p):
        c = self.unbal_c(p)
        if not c: return None
        self.swap(p, c); return c

    def swim(self, c):
        while c: c = self.lift(c)

    def sink(self, p):
        while p: p = self.drop(p)

    def heapify(self):
        for i in range(len(self), 0, -1): self.sink(i)

    def __setitem__(self, key, value):
        if key in self.dict:
            index = self.qp[key]
        else:
            self.pq.append(key)
            index = len(self)
        self.qp[key] = index; self.dict[key] = value
        self.swim(index); self.sink(index)

    def top_key(self): return self.pq[1]

    def top_val(self): return self.dict[self.top_key()]

    def top_item(self): return self.top_key(), self.top_val()

    def pop_item(self):
        self.swap(1, len(self))
        key, val = self.item(len(self))
        self.pq.pop()
        self.sink(1)
        self.qp.pop(key); self.dict.pop(key)
        return key, val

    def pop_key(self): return self.pop_item()[0]

    def pop_val(self): return self.pop_item()[1]

    def sorted_items(self):
        self.N = len(self)
        while self.N > 1:
            self.swap(1, self.N); self.N -= 1; self.sink(1)
        items = [self.item(i) for i in self.pq]
        self.N = None; self.heapify()
        return items

    def sorted_keys(self):
        return [map(lambda x: x[0], self.sorted_items())]

    def sorted_vals(self):
        return [map(lambda x: x[1], self.sorted_items())]

class Wedigraph:
    def __init__(self, V, es):
        self.V = V; self.adj = defaultdict(list)
        self.adds(es)

    def add(self, e):
        self.adj[e[0]].append(e)

    def adds(self, es):
        for e in es: self.add(e)


class DijkstraHeapq:
    def __init__(self, g, s):
        self.g = g; self.V = g.V
        self.dist_to = {v: float('inf') for v in range(1, self.V + 1)}
        self.dist_to[s] = 0; self.pq = []
        heappush(self.pq, (s, self.dist_to[s]))
        while self.pq:
            v, _ = heappop(self.pq)
            for e in self.g.adj[v]:
                self.relax(e)

    def relax(self, e):
        u, v, wt = e; du, dv = self.dist_to[u], self.dist_to[v]
        if dv > du + wt:
            self.dist_to[v] = du + wt
            heappush(self.pq, (v, self.dist_to[v]))

    def max_time(self):
        max_t = 0
        for v in range(1, self.V + 1):
            if self.dist_to[v] == float('inf'): return -1
            max_t = max(max_t, self.dist_to[v])
        return max_t


class DijkstraHeapDict:
    def __init__(self, g, s):
        self.g = g; self.V = g.V; self.adj = self.g.adj
        self.dist_to = {v: (0 if v == s else float('inf')) for v in range(1, self.V + 1)}
        self.pq = HeapDict(); self.pq[s] = self.dist_to[s]
        while self.pq:
            v = self.pq.pop_key()
            for e in self.adj[v]:
                self.relax(e)

    def relax(self, e):
        u, v, wt = e; du, dv = self.dist_to[u], self.dist_to[v]
        if dv > du + wt:
            self.dist_to[v] = du + wt
            self.pq[v] = self.dist_to[v]


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = Wedigraph(n, times); dijk = DijkstraHeapq(g, k)
        return dijk.max_time()