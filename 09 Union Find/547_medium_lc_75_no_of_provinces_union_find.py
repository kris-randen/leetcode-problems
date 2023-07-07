"""

547. Number of Provinces
Medium
8.5K
317
Companies
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.



Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

"""

class UnionFind:
    def __init__(self, n):
        self.size = n
        self.id = [i for i in range(n)]
        self.sz = [1 for _ in range(n)]
        self.num = n

    def parent(self, c):
        return self.id[c]

    def is_root(self, c):
        return self.parent(c) == c

    def assign(self, c, root):
        self.id[c] = root

    def size(self, r):
        return self.sz[r]

    def order(self, p, q):
        l, s = self.root(p), self.root(q)
        return (l, s) if self.size(l) > self.size(s) else (s, l)

    def path(self, c):
        path = [c]
        while not self.is_root(c):
            c = self.parent(c); path.append(c)
        return path

    def compress(self, c):
        path = self.path(c); root = path[-1]
        for i in path: self.assign(i, root)
        return root

    def root(self, c):
        return self.compress(c)

    def find(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        if self.find(p, q): return
        l, s = self.order(p, q)
        self.assign(s, l); self.sz[l] += self.sz[s]
        self.num -= 1


def provinces(cities):
    n = len(cities); uf = UnionFind(n)
    for i in range(n):
        cons = cities[i]
        for j, con in enumerate(cons):
            uf.union(i, j)
    return uf.num

