"""

199. Binary Tree Right Side View
Medium
10.4K
630
Companies
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.



Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []

"""
from functools import reduce
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def children(n):
    if not n.right and not n.left: return []
    if not n.left: return [n.right]
    if not n.right: return [n.left]
    return [n.right, n.left]

def children_list(ns):
    return reduce(lambda x, y: x + children(y), ns, [])


def right_side(node):
    if not node: return []
    q, res = [], []; q.append([node])
    while len(q) > 0:
        ns = q.pop()
        res.append(ns[0].val)
        cs = children_list(ns)
        if cs: q.append(cs)
    return res

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return right_side(root)