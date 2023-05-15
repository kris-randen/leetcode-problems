from typing import List


class UnionFind:
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.sz = [1 for i in range(n)]

    def root(self, i):
        while i is not self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def connected(self, i, j):
        return self.root[i] == self.root[j]

    def union(self, i, j):
        p = self.root(i)
        q = self.root(j)

        




class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return 0