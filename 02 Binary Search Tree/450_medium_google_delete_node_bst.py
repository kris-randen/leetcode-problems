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

# Delete Practice on 19th June 2023

def min_01(node):
    if not node: return None
    if not node.left: return node
    return min_01(node.left)


def delete_min_01(node):
    if not node: return None
    if not node.left: return node.right
    node.left = delete_min_01(node.left)
    return node

def delete_01(node, key):
    if not node: return None
    if key < node.val: node.left = delete_01(node.left, key)
    if key > node.val: node.right = delete_01(node.right, key)
    if key == node.val:
        if not node.left: return node.right
        if not node.right: return node.left
        t = node
        node = min(t.right)
        node.right = delete_min_01(t.right)
        node.left = t.left
    return node

# Delete Node BST Practice 02 9th Jul 2023

def min_02(x):
    if not x or not x.left: return x
    return min_02(x.left)

def delete_min_02(x):
    if not x: return None
    if not x.left: return x.right
    x.left = delete_min_02(x.left)
    return x

def delete_02(x, key):
    if not x: return x
    if key < x.val: x.left = delete_02(x.left, key)
    if key > x.val: x.right = delete_02(x.right, key)
    if key == x.val:
        if not x.left: return x.right
        if not x.right: return x.left
        t = x; x = min_02(t.right)
        x.right = delete_min_02(t.right)
        x.left = t.left
    return x










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




