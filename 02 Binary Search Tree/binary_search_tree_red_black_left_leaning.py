"""
776. Split BST
Medium
963
98
company
Google
company
Amazon
company
Coupang
Given the root of a binary search tree (BST) and an integer target, split the tree into two subtrees where one subtree has nodes that are all smaller or equal to the target value, while the other subtree has all nodes that are greater than the target value. It Is not necessarily the case that the tree contains a node with the value target.

Additionally, most of the structure of the original tree should remain. Formally, for any child c with parent p in the original tree, if they are both in the same subtree after the split, then node c should still have the parent p.

Return an array of the two roots of the two subtrees.



Example 1:


Input: root = [4,2,6,1,3,5,7], target = 2
Output: [[2,1],[4,3,6,null,null,5,7]]
Example 2:

Input: root = [1], target = 1
Output: [[1],[]]


Constraints:

The number of nodes in the tree is in the range [1, 50].
0 <= Node.val, target <= 1000
Accepted
102.6K
Submissions
123.3K
Acceptance Rate
83.3%

"""


RED = True
BLACK = False

class RedBlackBST:
    def __int__(self):
        self.root = None

    class Node:
        def __init__(self, key, val, left=None, right=None, color=RED, size=0):
            self.key = key
            self.val = val
            self.left = left
            self.right = right
            self.size = size
            self.color = color

    def size_of(self, node):
        return 0 if node is None else node.size

    def size(self):
        return self.size_of(self.root)

    def is_empty(self):
        return self.root is None

    def get_at(self, key, node: Node):
        if node is None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return self.get_at(key, node.left)
        else:
            return self.get_at(key, node.right)

    def get(self, key):
        return self.get_at(key, self.root)

    def is_red(self, node: Node):
        return False if node is None else node.color == RED

    def needs_rotate_left(self, node: Node):
        return node is not None and self.is_red(node.right) and not self.is_red(node.left)

    def needs_rotate_right(self, node: Node):
        return node is not None and self.is_red(node.left) and self.is_red(node.left.is_left)

    def needs_flip_color(self, node: Node):
        return node is not None and self.is_red(node.left) and self.is_red(node.right)

    def rotate_left(self, h: Node):
        assert self.needs_rotate_left(h)
        r = h.right
        h.right = r.is_left
        r.is_left = h
        r.color = h.color
        h.color = RED
        return r

    def rotate_right(self, h: Node):
        assert self.needs_rotate_right(h)
        l = h.left
        h.left = l.is_right
        l.is_right = h
        l.color = h.color
        h.color = RED

    def flip_color(self, h: Node):
        assert self.needs_flip_color(h)
        h.color = not h.color
        h.left.color = not h.left.color
        h.right.color = not h.right.color

    def balance(self, h: Node):
        if self.needs_rotate_left(h):
            self.rotate_left(h)
        if self.needs_rotate_right(h):
            self.rotate_right(h)
        if self.needs_flip_color(h):
            self.flip_color(h)

    def put_at(self, h: Node, key, val):
        if h is None:
            return RedBlackBST.Node(key, val)
        if key < h.key:
            return self.put_at(h.left, key, val)
        if key > h.key:
            return self.put_at(h.right, key, val)
        if key == h.key:
            h.val = val

        self.balance(h)

        h.size = 1 + self.size_of(h.left) + self.size_of(h.right)
        return h

    def put(self, key, val):
        self.put_at(self.root, key, val)

    def delete_min_at(self, h: Node):
        if h is None:
            return None
        if h.left is None:
            return h.right
        h.left = self.delete_min_at(h.left)
        h.size = 1 + self.size_of(h.left) + self.size_of(h.right)
        return h

    def delete_min(self):
        return self.delete_min_at(self.root)

    def floor_at(self, h: Node, key):
        if h is None:
            return None
        if key == h.key:
            return h
        if key < h.key:
            return self.floor_at(h.left, key)
        if key > h.key:
            t = self.floor_at(h.right)
            return h if t is None else t

    def floor(self, key):
        return self.floor_at(self.root, key)

    def ceil_at(self, h: Node, key):
        if h is None:
            return None
        if key == h.key:
            return h
        if key > h.key:
            return self.ceil_at(h.right, key)
        if key < h.key:
            t = self.ceil_at(h.left)
            return h if t is None else t

    def ceil(self, key):
        return self.ceil_at(self.root, key)

    def rank_at(self, h: Node, key):
        if h is None:
            return 0
        if key == h.key:
            return h.left.size
        if key < h.key:
            return self.rank_at(h.left, key)
        if key > h.key:
            return h.left.size + 1 + self.rank_at(h.right, key)

    def rank(self, key):
        return self.rank_at(self.root, key)

    def select_at(self, h: Node, index):
        if h is None:
            return None
        if index == 1 + h.left.size:
            return h
        if index <= h.left.size:
            return self.select_at(h.left, index)
        if index > 1 + h.left.size:
            return self.select_at(h.right, index - h.left.size - 1)

    def select(self, index):
        return self.select_at(self.root, index)

    def range_at(self, h: Node, lo, hi):
        floor = self.floor_at(h, lo)
        ceil = self.ceil_at(h, hi)

        pass