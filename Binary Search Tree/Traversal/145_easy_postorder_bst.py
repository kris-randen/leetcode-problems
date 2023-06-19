"""
145. Binary Tree Postorder Traversal
Easy
6K
174
company
Yahoo
company
Apple
company
Facebook
Given the root of a binary tree, return the postorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
"""

def postorder(node, path):
    if not node: return
    postorder(node.left, path)
    postorder(node.right, path)
    path.append(node.val)