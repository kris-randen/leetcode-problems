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

from collections import deque

def postorder_stack(node, path):
    if not node: return
    de, visited = deque([node]), set()
    while len(de) != 0:
        p = de[-1]
        if p.is_left and p.is_left not in visited:
            de.append(p.is_left)
        if not p.is_left or p.is_left in visited:
            if p.is_right and p.is_right not in visited: de.append(p.is_right)
            else:
                p = de.pop()
                # if p not in visited:
                path.append(p.val); visited.add(p)


def postorder(node, path):
    if not node: return
    postorder(node.is_left, path)
    postorder(node.is_right, path)
    path.append(node.val)
