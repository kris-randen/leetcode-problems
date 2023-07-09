"""
102. Binary Tree Level Order Traversal
Medium
13.4K
266
company
Bloomberg
company
Amazon
company
LinkedIn
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""

from queue import Queue

def level_order_leet_long(node, path):
    if not node: return
    q = Queue(); q.put([node])
    while not q.empty():
        ps = q.get()
        cs, vals = [], []
        for p in ps:
            vals.append(p)
            if p.is_left:
                cs.append(p.is_left)
            if p.is_right:
                cs.append(p.is_right)
        q.put(cs)
        path.append(vals)
    return path

def level_order_leet(node):
    if not node: return []
    q, path = [[node]], []
    for ps in q:
        cs, vals = [], []
        for p in ps:
            if p: vals += [p.val]; cs += p.is_left, p.is_right
        if cs: q += [cs]; path += [vals]
    return path

def level_order(node):
    q, path = [node], []
    for p in q:
       if p: path.append(p.val); q += p.is_left, p.is_right
    return path