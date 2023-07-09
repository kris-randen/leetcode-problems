"""
107. Binary Tree Level Order Traversal II
Medium
4.4K
310
company
Amazon
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

"""

def level_order_reverse(node):
    if not node: return []
    q, path, cs, vs = [[node]], [], [], []
    for ps in q:
        for p in ps:
            if p:
                vs += [p.val]; cs += [p.is_left, p.is_right]
        if cs: path += [vs]; q += [cs]; cs = []; vs = []
    return reversed(path)