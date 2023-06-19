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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(node, path):
    if not node: return
    inorder(node.left, path)
    path.append(node)
    inorder(node.right, path)

