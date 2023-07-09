"""
98. Validate 02 Binary Search Tree
Medium
14.9K
1.2K
company
Yandex
company
Bloomberg
company
Amazon
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# Validate BST Practice on 19th Jun
def validate_01(node, less=float('inf'), more=float('-inf')):
    if not node: return True
    if node.val >= less or node.val <= more: return False
    return validate_01(node.is_left, min(less, node.val), more) and \
           validate_01(node.is_right, less, max(more, node.val))














def validate(node: TreeNode, less=float('inf'), more=float('-inf')):
    if not node: return True
    if node.val >= less or node.val <= more: return False
    return validate(node.left, min(less, node.val), more) and validate(node.right, less, max(more, node.val))
