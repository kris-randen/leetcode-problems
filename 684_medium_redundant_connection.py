"""

684. Redundant Connection
Medium
5.2K
351
Companies

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.



Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]


Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
Accepted
273.5K
Submissions
438.9K
Acceptance Rate
62.3%

"""
from typing import List


class UnionFind:
    def __init__(self, n, count=None):
        self.__n = n
        self.__id = [i for i in range(self.__n)]
        self.__sz = [1 for i in range(self.__n)]
        self.__count = self.__n if count is None else count

    def __parent(self, node):
        return self.__id[node]

    def __assign(self, node, parent):
        self.__id[node] = parent

    def __path(self, node):
        path = [node]
        while node != self.__parent(node):
            node = self.__parent(node)
            path.append(node)
        return path

    def __root(self, path):
        return path[-1]

    def __compress(self, path):
        for node in path:
            self.__assign(node, self.__root(path))

    def __size(self, root):
        return self.__sz[root]

    def __size_up(self, small, large):
        self.__sz[large] += self.__sz[small]

    def __order_components(self, a, b):
        p, q = self.find(a), self.find(b)
        small = p if self.__size(p) < self.__size(q) else q
        large = q if self.__size(q) > self.__size(p) else p
        return small, large

    def size(self):
        return self.__n

    def root(self, node):
        path = self.__path(node)
        self.__compress(path)
        return self.__root(path)

    def find(self, node):
        return self.root(node)

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        if self.connected(a, b):
            return 1
        small, large = self.__order_components(a, b)
        self.__assign(small, large)
        self.__size_up(small, large)
        self.__count -= 1
        return None

def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    graph = UnionFind(len(edges))
    redundant = []
    for edge in edges:
        if graph.union(edge[0]-1, edge[1]-1):
            redundant.append(edge)
    return redundant[-1]

if __name__ == '__main__':
    print(findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))