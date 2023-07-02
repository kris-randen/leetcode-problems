from functools import reduce
from typing import List

class Node:
    def __init__(self, val, parent=None, children=None, root=None):
        self.val = val
        self.parent = parent
        self.children = [] if children is None else children
        self.root = self if root is None else root

    def assign_root(self, root) -> bool:
        if self.root is root:
            return False
        self.root = root
        for child in self.children:
            child.assign_root(root)
        return True

class UnionFindGraph:
    def __init__(self, n, count=None):
        self.n = n
        self.nodes = [Node(i) for i in range(n)]
        self.comps = {root: [root] for root in self.nodes}
        self.count = len(self.comps)

    def add_edge(self, parent_index, child_index) -> bool:
        parent = self.nodes[parent_index]
        child = self.nodes[child_index]
        child.parent = parent
        parent.children.append(child)
        return child.assign_root(parent.root)

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        graph = UnionFindGraph(len(edges))
        redundant = []
        for edge in edges:
            if not graph.add_edge(edge[0]-1, edge[1]-1):
                redundant.append(edge)
        return redundant[-1]