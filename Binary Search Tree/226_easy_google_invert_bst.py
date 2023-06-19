"""
226. Invert Binary Tree
Easy
12.3K
174
company
Google
company
Amazon
company
Apple
Given the root of a binary tree, invert the tree, and return its root.



Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
Accepted
1.6M
Submissions
2.1M
Acceptance Rate
75.0%
"""

# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert(node):
    if node is None:
        return None
    l = node.left
    r = node.right
    node.left = invert(r)
    node.right = invert(l)
    return node

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return invert(root)