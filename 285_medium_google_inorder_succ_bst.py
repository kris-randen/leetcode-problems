"""
285. Inorder Successor in BST
Medium
2.4K
87
company
Microsoft
company
Arista Networks
company
Facebook
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.



Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorder_succ(node, key):
    if not node: return None
    if key < node.val:
        t = inorder_succ(node.left, key)
        return t if t is not None else TreeNode(node.val)
    if key > node.val: return inorder_succ(node.right, key)
    if key == node.val:
        l, r = inorder_succ(node.left, key), inorder_succ(node.right, key)
        if not l and not r: return None
        if not l: return r
        if not r: return l

