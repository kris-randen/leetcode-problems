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

def preorder_stack(node, path):
    if not node: return
    de, visited = deque([node]), set()
    while len(de) != 0:
        p = de[-1]
        if p not in visited:
            path.append(p.val); visited.add(p)
        else: p = de.pop()
        if p.left and p.left not in visited:
            de.append(p.left)
        if not p.left or p.left in visited:
            if p.right and p.right not in visited:
                de.append(p.right)
            else: continue


def preorder(node, path):
    if not node: return
    path.append(node.val)
    preorder(node.left, path)
    preorder(node.right, path)

