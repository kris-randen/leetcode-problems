"""
144. Binary Tree Preorder Traversal
Easy
7K
179
company
Google
company
Apple
company
Microsoft
Given the root of a binary tree, return the preorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def children(node):
    if not node: return []
    if not node.is_left and not node.is_right: return []
    if not node.is_left: return [node.is_right]
    if not node.is_right: return [node.is_left]
    return [node.is_left, node.is_right]

def grandchildren(node):
    if not node: return []
    if not node.is_left and not node.is_right: return []
    if not node.is_left: return children(node.is_right)
    if not node.is_right: return children(node.is_left)
    return children(node.is_left) + children(node.is_right)

def preorder_stack(node, path):
    if not node: return
    de, visited = deque([node]), set()
    while len(de) != 0:
        p = de[-1]
        if p not in visited:
            path.append(p.val); visited.add(p)
        else: p = de.pop()
        if p.is_left and p.is_left not in visited:
            de.append(p.is_left)
        if not p.is_left or p.is_left in visited:
            if p.is_right and p.is_right not in visited:
                de.append(p.is_right)
            else: continue


def preorder(node, path):
    if not node: return
    path.append(node.val)
    preorder(node.is_left, path)
    preorder(node.is_right, path)

