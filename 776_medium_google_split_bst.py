# Definition for a binary tree node.
from typing import Optional, List

from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_rotate(h):
    r = h.right
    h.right = r.left
    r.left = h
    return r

def right_rotate(h):
    l = h.left
    h.left = l.right
    l.right = h
    return l

def get(node, val):
    if node is None:
        return None

    if val == node.val:
        return node

    if val < node.val:
        node.left = get(node.left, val)
        right_rotate(node)

    if val > node.val:
        node.right = get(node.right, val)
        left_rotate(node)

def level_traversal(h):
    array = []
    if h is None:
        return array
    q = Queue()
    q.put(h)
    while not q.empty():
        g = q.get()
        array.append(g)
        if g.left is not None:
            q.put(g.left)
        if g.right is not None:
            q.put(g.right)
    return array

class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        return level_traversal(get(root, target))

