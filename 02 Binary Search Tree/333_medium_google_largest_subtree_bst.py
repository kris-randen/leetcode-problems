"""
333. Largest BST Subtree
Medium
1.4K
112
company
Amazon
company
ByteDance
company
Facebook
Given the root of a binary tree, find the largest
subtree
, which is also a 02 Binary Search Tree (BST), where the largest means subtree has the largest number of nodes.

A 02 Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties:

The left subtree values are less than the value of their parent (root) node's value.
The right subtree values are greater than the value of their parent (root) node's value.
Note: A subtree must include all of its descendants.



Example 1:



Input: root = [10,5,15,1,8,null,7]
Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one. The return value is the subtree's size, which is 3.
Example 2:

Input: root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
Output: 2
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def size(node: TreeNode):
    if not node: return 0
    return 1 + size(node.left) + size(node.right)

def validate(node: TreeNode, less=float('inf'), more=float('-inf')):
    if not node: return True
    if node.val >= less or node.val <= more: return False
    return validate(node.left, min(less, node.val), more) and \
           validate(node.right, less, max(more, node.val))

def max_bst_sub(node: TreeNode):
    if not node: return 0
    if validate(node): return size(node)
    return max(max_bst_sub(node.left), max_bst_sub(node.right))





