"""
124. Binary Tree Maximum Path Sum
Hard
14.4K
654
company
Amazon
company
Adobe
company
Booking.com
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.



Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

"""


def max_path_sum(root):
    max_sum = float('-inf')

    def path_sum(node):
        nonlocal max_sum
        if not node: return 0
        l, r = path_sum(node.left), path_sum(node.right)
        left, right = max(l, 0), max(r, 0)
        max_sum = max(max_sum, left + right + node.val)
        return max(left + node.val, right + node.val)

    path_sum(root)
    return max_sum

