"""
2476. Closest Nodes Queries in a Binary Search Tree
Medium
329
86
company
Google
You are given the root of a binary search tree and an array queries of size n consisting of positive integers.

Find a 2D array answer of size n where answer[i] = [mini, maxi]:

mini is the largest value in the tree that is smaller than or equal to queries[i]. If a such value does not exist, add -1 instead.
maxi is the smallest value in the tree that is greater than or equal to queries[i]. If a such value does not exist, add -1 instead.
Return the array answer.



Example 1:


Input: root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]
Output: [[2,2],[4,6],[15,-1]]
Explanation: We answer the queries in the following way:
- The largest number that is smaller or equal than 2 in the tree is 2, and the smallest number that is greater or equal than 2 is still 2. So the answer for the first query is [2,2].
- The largest number that is smaller or equal than 5 in the tree is 4, and the smallest number that is greater or equal than 5 is 6. So the answer for the second query is [4,6].
- The largest number that is smaller or equal than 16 in the tree is 15, and the smallest number that is greater or equal than 16 does not exist. So the answer for the third query is [15,-1].
Example 2:


Input: root = [4,null,9], queries = [3]
Output: [[-1,4]]
Explanation: The largest number that is smaller or equal to 3 in the tree does not exist, and the smallest number that is greater or equal to 3 is 4. So the answer for the query is [-1,4].
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.rigt = right

def ceil(node, key):
    if not node: return None
    if node.val == key: return node.val
    if key > node.val:
        if node.right: return ceil(node.right, key)
        else: return None
    t = ceil(node.left, key)
    return t if t is not None else node.val


def floor(node, key):
    if not node: return None
    if node.val == key: return node.val
    if key < node.val:
        if node.left: return floor(node.left, key)
        else: return None
    t = floor(node.right, key)
    return t if t is not None else node.val

# def closest(node, queries, indices, answers):
#     if not node: return
#     left, right = [], []
#     for i in indices:
#         if queries[i] == node.val: answers[i] = [node.val, node.val]
#         if queries[i] > node.val:
#             if not node.right:
#                 answers[i][0], answers[i][1] = node.val, -1
#             else:
#                 right.append(i)
#         if queries[i] < node.val:
#             if not node.left:
#                 answers[i][0], answers[i][1] = -1, node.val
#             else:
#                 left.append(i)

def ceils(node, queries, indices, answers):
    if not node: return
    left, right = [], []
    for i in indices:
        if queries[i] == node.val: answers[i][1] = node.val
        if queries[i] > node.val:
            if not node.right: answers[i][1] = -1
            else: right.append(i)
        if queries[i] < node.val:
            if not node.left: answers[i][1] = node.val
            else: left.append(i)
    if node.left:
        ceils(node.left, queries, left, answers)
        for i in left:
            answers[i][1] = node.val if answers[i][1] == -1 else answers[i][1]
    if node.right:
        ceils(node.right, queries, right, answers)

def floors(node, queries, indices, answers):
    if not node: return
    left, right = [], []
    for i in indices:
        if queries[i] == node.val: answers[i][0] = node.val
        if queries[i] > node.val:
            if not node.right: answers[i][0] = node.val
            else: right.append(i)
        if queries[i] < node.val:
            if not node.left: answers[i][0] = -1
            else: left.append(i)
    if node.left:
        floors(node.left, queries, left, answers)
    if node.right:
        floors(node.right, queries, right, answers)
        for i in right:
            answers[i][0] = node.val if answers[i][0] == -1 else answers[i][0]

def closest(node, queries):
    n = len(queries)
    indices, answers = [_ for _ in range(n)], [[-1, -1] for _ in range(n)]
    floors(node, queries, indices, answers)
    ceils(node, queries, indices, answers)
    return answers
