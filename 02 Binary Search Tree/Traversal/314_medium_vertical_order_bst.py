"""
314. Binary Tree Vertical Order Traversal
Medium
2.9K
293
company
Facebook
company
Bloomberg
company
Amazon
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]

"""
import heapq
from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


from queue import Queue


class Node:
    def __init__(self, p: TreeNode, col=0):
        self.node = p
        self.col = col


def children(node: Node):
    if not node: return []
    if not node.node.left and not node.node.right: return []
    if not node.node.left: return [Node(node.node.right, node.col + 1)]
    if not node.node.right: return [Node(node.node.left, node.col - 1)]
    return [Node(node.node.left, node.col - 1), Node(node.node.right, node.col + 1)]


def level_order_col(root):
    if not root: return []
    q, path = Queue(), []; q.put([Node(root, 0)])
    while not q.empty():
        ps, cs, vals = q.get(), [], []
        for p in ps:
            vals.append(Node(p.node, p.col))
            cs += children(p)
        if cs: q.put(cs)
        path.append(vals)
    return path


def convert(nodess):
    pq = []
    for nodes in nodess:
        for node in nodes:
            pq.append(node)
    pq.sort(key=lambda x: x.col)
    return pq


def collect(nodes):
    items = {}
    for node in nodes:
        if node.col not in items:
            items[node.col] = [node]
        else:
            items[node.col].append(node)
    return items


def vertical_order_long(node):
    if not node: return []
    path, c, vals = [], [], []
    path = level_order_col(node)
    converted = convert(path)

    collected = collect(converted)

    keys = list(collected.keys())
    keys.sort()

    for key in keys:
        nodes = collected[key]
        vals = []
        for n in nodes:
            vals.append(n.node.val)
        c.append(vals)
    return c

from collections import defaultdict

def vertical_order(node):
    cols, q = defaultdict(list), [(node, 0)]
    for p, i in q:
        if p: cols[i].append(p.val); q += (p.is_left, i - 1), (p.is_right, i + 1)
    return [cols[i] for i in sorted(cols)]





