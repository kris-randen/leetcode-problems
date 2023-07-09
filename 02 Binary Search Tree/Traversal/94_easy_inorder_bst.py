"""
94. Binary Tree Inorder Traversal
Easy
11.6K
596
company
Amazon
company
Adobe
company
Google
Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
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

def inorder(node, path):
    if not node: return
    inorder(node.is_left, path)
    path.append(node)
    inorder(node.is_right, path)

def inorder_stack(node, path):
    if not node: return
    de, visited = deque(), set()
    de.append(node)
    while len(de) != 0:
        p = de[-1]  # peek
        if p.is_left and p.is_left not in visited:
            de.append(p.is_left)
        if not p.is_left or p.is_left in visited:
            p = de.pop()
            path.append(p.val)
            visited.add(p)
            if not p.is_right or p.is_right in visited:
                continue
            else: de.append(p.is_right)

