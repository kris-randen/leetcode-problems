"""
103. Binary Tree Zigzag Level Order Traversal
Medium
9.4K
245
company
Amazon
company
Bloomberg
company
Microsoft
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

"""

def zigzag(node):
    if not node: return []
    q, r, level, cs, vs = [[node]], [], 0, [], []
    for ps in q:
        for p in ps:
            if p: vs += [p.val]; ds = [p.is_left, p.is_right]; cs += ds
        if cs:
            vs = vs if level % 2 == 0 else reversed(vs)
            q += [cs]; r += [vs]; level += 1; cs = []; vs = []
    return r


