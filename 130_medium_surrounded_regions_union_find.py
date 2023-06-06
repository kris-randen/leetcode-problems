"""
130. Surrounded Regions
Medium
7.1K
1.5K
Companies
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.



Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
Accepted
537.5K
Submissions
1.5M
Acceptance Rate
37.0%

"""

from typing import List

class Point:
    LEFT = 0, -1
    RIGHT = 0, 1
    UP = -1, 0
    DOWN = 1, 0

    def __init__(self, i, j, val=None):
        self.i = i
        self.j = j
        self.val = val

    def add(self, point):
        return Point(self.i + point.i, self.j + point.j)

    def left(self):
        return self.add(Point(*Point.LEFT))

    def right(self):
        return self.add(Point(*Point.RIGHT))

    def up(self):
        return self.add(Point(*Point.UP))

    def down(self):
        return self.add(Point(*Point.DOWN))

    def neighbors(self):
        return [self.left(), self.right(), self.up(), self.down()]

class Board:
    def __init__(self, matrix):
        self.matrix = matrix
        self.height, self.width, self.area = self.dimensions(matrix)

    def dimensions(self, board):
        height = len(board)
        width = len(board[0])
        area = height * width
        return height, width, area

    def is_valid(self, point):
        return 0 <= point.i < self.height and 0 <= point.j < self.width

    def valid(self, point):
        return point if self.is_valid(point) else None

    def left(self, point):
        return self.valid(point.left())

    def right(self, point):
        return self.valid(point.right())

    def up(self, point):
        return self.valid(point.up())

    def down(self, point):
        return self.valid(point.down())

    def neighbors(self, point):
        return list(filter(self.is_valid, point.neighbors()))

    def value(self, n):
        point = self.point(n)
        return self.matrix[point.i][point.j] if self.is_valid(point) else None

    def point(self, n):
        return self.valid(Point(n/self.width, (n % self.width) - 1, val=self.value(n)))

    def flatten(self, point):
        return (point.i * self.width) + point.j + 1


class UnionFind2D:
    def __init__(self, matrix, marker=None):
        self.board = Board(matrix)
        self.id = [i for i in range(self.board.area)]
        self.marker = marker
        self.marked = list(filter(self.is_marked, self.id))
        self.val = [self.board.value(i) for i in self.id]
        self.comps = {root: [root] for root in self.id}

    def is_marked(self, node):
        return self.board.value(node) == self.marker

    def parent(self, node):
        return self.id[node]

    def assign_parent(self, node, parent):
        self.id[node] = parent

    def path(self, node):
        path = [node]
        while node != self.parent(node):
            node = self.parent(node)
            path.append(node)
        return path

    def root(self, node):
        return self.path(node)[-1]

    def compressed_root(self, node):
        path = self.path(node)
        root = path[-1]
        for point in path:
            self.assign_parent(point, root)
        return root

    def find(self, p, q):
        return self.compressed_root(p) == self.compressed_root(q)

    def size(self, root):
        return len(self.comps[root])

    def order(self, p, q):
        child = p if self.size(p) < self.size(q) else q
        parent = q if self.size(q) > self.size(p) else p
        return child, parent

    def update(self, small, large):
        self.comps[large] += self.comps.pop(small)

    def union(self, p, q):
        if self.find(p, q):
            return
        child, parent = self.order(p, q)
        self.assign_parent(child, parent)
        self.update(child, parent)

    def visit(self, is_valid):
        for node in self.marked:
            point = self.board.point(node)
            neighbors = self.board.neighbors(point)
            for neighbor in neighbors:
                adjacent = self.board.flatten(neighbor)
                if is_valid(neighbor):
                    self.union(node, adjacent)

    def unite(self):
        self.visit(self.is_marked)

    def surrounding(self, node):
        point = self.board.point(node)
        neighbors = self.board.neighbors(point)
        for neighbor in neighbors:
            pass

    def capture(self, node, mark=None):
        pass



class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        graph = UnionFind2D(board, marker="O")
        graph.unite()
