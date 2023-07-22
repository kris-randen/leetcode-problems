"""

1631. Path With Minimum Effort
Medium
4.6K
159
Companies
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.



Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.

"""

from heapq import *
from collections import defaultdict
from typing import List

def unwrap(a, default):
    return a if a else default

class HeapDict:
    def __init__(self, order=None):
        self.pq, self.qp, self.dict, self.N = [-1], {}, {}, None
        self.order = order if order else (lambda x, y: x if x < y else y)

    def key(self, i): return self.pq[i]

    def val(self, i): return self.dict[self.key(i)]

    def item(self, i): return self.key(i), self.val(i)

    def __len__(self): return unwrap(self.N, len(self.pq) - 1)

    def is_empty(self): return len(self) == 0

    def is_valid(self, i): return 1 <= i <= len(self)

    def valid(self, i): return i if self.is_valid(i) else None

    def ord(self, i, j): return i if self.order(self.val(i), self.val(j)) == self.val(i) else j

    def swap(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]], self.qp[self.pq[j]] = i, j

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
        c = self.child(p)
        if not c: return True
        return self.pref(p, c) == p

    def unbal_p(self, c):
        if not self.bal_up(c): return self.parent(c)

    def unbal_c(self, p):
        if not self.bal_dn(p): return self.child(p)

    def lift(self, c):
        if not self.bal_up(c): p = self.parent(c); self.swap(p, c); return p

    def drop(self, p):
        if not self.bal_dn(p): c = self.child(p); self.swap(p, c); return c

    def swim(self, c):
        while c: c = self.lift(c)

    def sink(self, p):
        while p: p = self.drop(p)

    def pop_item(self):
        ind = len(self); self.swap(1, len(self))
        key, val = self.key(ind), self.val(ind)
        self.pq.pop(ind); self.qp.pop(key); self.dict.pop(key)
        self.sink(1); return key, val

    def pop_key(self): return self.pop_item()[0]

    def pop_val(self): return self.pop_item()[1]

    def contains(self, key): return key in self.dict

    def __getitem__(self, key): return self.dict[key]

    def __setitem__(self, key, value):
        if key not in self.dict: self.pq.append(key)
        ind = self.qp[key] if self.contains(key) else len(self)
        self.qp[key] = ind; self.dict[key] = value
        self.swim(ind); self.sink(ind)



class Graph:
    def __init__(self, hs):
        self.hs = hs; self.m, self.n = len(hs), len(hs[0]); self.V = self.m * self.n;
        self.adj = defaultdict(set); self.s = 0; self.t = self.V - 1
        for v in range(self.V):
            p = self.rise(v); ns = self.nbs(p)
            for n in ns:
                wt = self.weight(p, n); w = self.flatten(n)
                self.adj[v].add((v, w, wt))

    def weight(self, u, v): return abs(self.val(u) - self.val(v))

    def val(self, p): return self.hs[p[0]][p[1]]

    def flatten(self, p): return (self.n * p[0]) + p[1]

    def rise(self, k): return (k // self.n), (k % self.n)

    def valid(self, p): return 0 <= p[0] < self.m and 0 <= p[1] < self.n

    def up(self, p): return p[0] - 1, p[1]

    def dn(self, p): return p[0] + 1, p[1]

    def lt(self, p): return p[0], p[1] - 1

    def rt(self, p): return p[0], p[1] + 1

    def nbs(self, p): return list(filter(lambda x: self.valid(x), [self.up(p), self.dn(p), self.lt(p), self.rt(p)]))

class DijkstraHeapq:
    def __init__(self, g, s, t):
        self.g, self.V, self.adj, self.pq, self.visited = g, g.V, g.adj, [], set()
        self.dist_to = [(0 if i == s else float('inf')) for i in range(self.V)]
        heappush(self.pq, (s, self.dist_to[s]))
        while self.pq:
            v, _ = heappop(self.pq)
            for e in self.g.adj[v]: self.relax(e)

    def path_sum(self, du, wt): return max(du, wt)

    def relax(self, e):
        u, v, wt = e; du, dv = self.dist_to[u], self.dist_to[v]; ps = self.path_sum(du, wt)
        if dv > ps:
            self.dist_to[v] = ps
            heappush(self.pq, (v, self.dist_to[v]))


class Dijkstra:
    def __init__(self, g, s, t):
        self.g, self.V, self.adj = g, g.V, g.adj; self.vs = range(self.V)
        self.dt = [(0 if v == s else float('inf')) for v in self.vs]
        self.pq = HeapDict(); self.pq[s] = self.dt[s]
        while self.pq:
            v = self.pq.pop_key()
            for e in self.adj[v]: self.relax(e)

    def p_sum(self, du, wt): return max(du, wt)

    def relax(self, e):
        u, v, wt = e; du, dv = self.dt[u], self.dt[v]; ps = self.p_sum(du, wt)
        if dv > ps:
            self.dt[v] = ps; self.pq[v] = ps



class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        g = Graph(heights); dijk = DijkstraHeapq(g, g.s, g.t)
        return dijk.dist_to[g.t]
