"""
450. Delete Node in a BST
Medium
7.6K
197
company
Amazon
company
Adobe
company
Apple
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.


Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
"""

def find(node, key):
    if not node: return None
    if key == node.val: return node.val
    if key < node.val: return find(node.left, key)
    if key > node.val: return find(node.right, key)

def get_min(node):
    if not node: return None
    if not node.left: return node.val
    return get_min(node.left)

def delete_min(node):
    if not node: return None
    if not node.left: return node.right
    node.left = delete_min(node.left)
    return node


def delete(node, key):
    if not node: return None
    if key < node.val: node.left = delete(node.left, key)
    if key > node.val: node.right = delete(node.right, key)
    if not node.left: return node.right
    if not node.right: return node.left
    t = node
    node = get_min(t.right)
    node.right = delete_min(t.right)
    node.left = t.left
    return node




