from functools import reduce
from typing import List

class UnionFind:
    def __init__(self, n, count=None):
        self.size = n
        self.indices = range(self.size)
        self.id = [i for i in self.indices]
        self.sz = [1 for i in self.indices]
        self.count = self.size if count is None else count

    def parent(self, node):
        parent = self.id[node]
        while node != parent:
            yield self.id[node]

    def path(self, node):
        pass

    def root(self, node):
        pass

    def root(self, i):
        #Defining path while traversing up for path compression
        path = [i]
        while i != self.id[i]:
            #Traversing up
            i = self.id[i]
            path.append(i)

        #Now we are at the root, so we return i but before that
        #we make sure to compress the path

        for node in path:
            self.id[node] = i

        return i




class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        return [0]