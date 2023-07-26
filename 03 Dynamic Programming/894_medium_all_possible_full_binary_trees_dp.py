"""

894. All Possible Full Binary Trees
Medium
4.6K
308
Companies
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.



Example 1:


Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Example 2:

Input: n = 3
Output: [[0,0,0]]

"""
from typing import List, Optional

def string(node):
    q = [[node]]
    s = ''
    s += node.val
    pass

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        s = ''

        pass

def is_leaf(node):
    return not node.left and not node.right

def leaves_of(node, ind):
    if not node or is_leaf(node): return [ind]
    return leaves_of(node.left, 2 * ind) + leaves_of(node.right, 2 * ind + 1)

def leaves(root):
    return leaves_of(root, 1)


def copy(tree):
    if not tree: return None
    root = TreeNode()
    root.left = copy(tree.left)
    root.right = copy(tree.right)
    return root

def parent(ind):
    return ind // 2, ind % 2

def path(root, ind):
    if ind == 1: return []
    p, d = parent(ind)
    return [d] + path(root, p)

def find(root, path):
    node = root
    for i in reversed(range(len(path))):
        if i == 0: node = node.left
        else: node = node.right
    return node

def all_trees(n):
    pr = [TreeNode()]; nt = []
    for i in range(1, n):
        for t in pr:
            ls = leaves(t)
            for l in ls:
                s = copy(t); ps = path(s, l); node = find(s, ps)
                node.left = TreeNode(); node.right = TreeNode()
                nt.append(s)
        pr = nt; nt = []
    return pr


if __name__ == '__main__':
    print(0)
    t = TreeNode()
    t.left = TreeNode(); t.right = TreeNode(); t.left.left = TreeNode(); t.left.right = TreeNode()
    s = copy(t); s.left.right.left = TreeNode(); s.left.right.right = TreeNode()
    print(leaves(t))
    print(leaves(s))
    print(t.left.val)

