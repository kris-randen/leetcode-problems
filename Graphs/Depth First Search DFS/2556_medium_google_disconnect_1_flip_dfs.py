"""
2556. Disconnect Path in a Binary Matrix by at Most One Flip
Medium
430
17
company
Google
You are given a 0-indexed m x n binary matrix grid. You can move from a cell (row, col) to any of the cells (row + 1, col) or (row, col + 1) that has the value 1. The matrix is disconnected if there is no path from (0, 0) to (m - 1, n - 1).

You can flip the value of at most one (possibly none) cell. You cannot flip the cells (0, 0) and (m - 1, n - 1).

Return true if it is possible to make the matrix disconnect or false otherwise.

Note that flipping a cell changes its value from 0 to 1 or from 1 to 0.



Example 1:


Input: grid = [[1,1,1],[1,0,0],[1,1,1]]
Output: true
Explanation: We can change the cell shown in the diagram above. There is no path from (0, 0) to (2, 2) in the resulting grid.
Example 2:


Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: false
Explanation: It is not possible to change at most one cell such that there is not path from (0, 0) to (2, 2).

"""

from enum import Enum


class PointType(Enum):
    INTERIOR = 1
    LEFT = 2
    TOP = 3
    RIGHT = 4
    BOTTOM = 5
    TOP_LEFT = 6
    TOP_RIGHT = 7
    BOTTOM_RIGHT = 8
    BOTTOM_LEFT = 9
    INVALID = 10


class Graph:
    def __init__(self, grid):
        self.grid, self.m, self.n = grid, len(grid), len(grid[0])
        self.V = self.m * self.n
        self.adjs = [[] for _ in range(self.V)]
        print(f'length of adjs = {len(self.adjs)}')
        self.add_edges()
        for line in grid: print(line)
        print(self.adjs)

    def add_edges(self):
        for i in range(self.m):
            for j in range(self.n):
                if not self.grid[i][j]: continue
                adj_ij = self.valid_adj(i, j)
                print(f'for i = {i}, j = {j}, adj = {adj_ij}')
                if not adj_ij: continue
                v = self.flatten((i, j))
                adj = map(lambda x: self.flatten(x), adj_ij)
                for w in adj:
                    print(f'adding edge v {v}, w {w}')
                    self.add_edge(v, w)

    def flatten(self, p):
        return (self.n * p[0]) + p[1]

    def expand(self, v):
        return (v // self.m), (v % self.n)

    def value(self, p):
        i, j = p; p_type = self.point_type(i, j)
        return None if p_type is PointType.INVALID else self.grid[i][j]

    def legit(self, ps, vals):
        if not vals[0] and not vals[1]: return None
        if not vals[0]: return [ps[1]]
        if not vals[1]: return [ps[0]]
        return ps

    def valid_adj(self, i, j):
        p_type = self.point_type(i, j)
        bottom, right = (i + 1, j), (i, j + 1)
        vb, vr = self.value(bottom), self.value(right)
        ps, vs = [bottom, right], [vb, vr]
        print(f'point type for v = [{i, j}] = {p_type}')
        print(f'ps {ps}, vs {vs}')
        if not vr and not vb: return None
        match p_type:
            case PointType.INVALID | PointType.BOTTOM_RIGHT:
                return None
            case PointType.TOP_RIGHT: return self.legit(ps, vs)
            case PointType.BOTTOM_LEFT: return self.legit(ps, vs)
            case PointType.TOP_LEFT | PointType.LEFT | PointType.TOP | PointType.INTERIOR:
                return self.legit(ps, vs)
            case PointType.RIGHT: return self.legit(ps, vs)
            case PointType.BOTTOM: return self.legit(ps, vs)


    def point_type(self, i, j):
        if not 0 <= i <= self.m - 1 or not 0 <= j <= self.n - 1:
            return PointType.INVALID

        if 0 < i < self.m - 1 and 0 < j < self.n - 1:
            return PointType.INTERIOR

        if not i and not j:
            return PointType.TOP_LEFT

        if not i and j == self.n - 1:
            return PointType.TOP_RIGHT

        if not j and i == self.m - 1:
            return PointType.BOTTOM_LEFT

        if i == self.m - 1 and j == self.n - 1:
            return PointType.BOTTOM_RIGHT

        if not i: return PointType.TOP
        if not j: return PointType.LEFT
        if i == self.m - 1: return PointType.BOTTOM
        if j == self.n - 1: return PointType.RIGHT

    def add_edge(self, v, w):
        self.adjs[v].append(w)

    def adj(self, v):
        return self.adjs[v]

    def V(self):
        return self.V

    def __str__(self):
        return ""


class DFS:
    def __init__(self, graph: Graph):
        self.g = graph
        self.visited = set()

    def num_paths_flat(self, s, t):
        adjs, paths = self.g.adj(s), 0
        print(f'for s {s}, t {t}, adjs = {adjs}, paths = {paths}')
        for v in adjs:
            print(f'v {v}')
            found = [False]
            self.dfs(v, t, found)
            if found[0]:
                print(f'path found for v {v}')
                paths += 1
        print(f'paths = {paths}')
        return paths

    def num_paths(self, p, q):
        print(f'num paths called for p {p}, q {q}')
        return self.num_paths_flat(self.g.flatten(p), self.g.flatten(q))

    def dfs(self, s, t, found):
        print(f'starting dfs for s: {self.g.expand(s)}')
        print(f'visited = {self.visited}')
        if s in self.visited: return
        if s == t:
            print(f'path found')
            found[0] = True
            return
        self.visited.add(s)
        print(f's {s}, t {t}')
        if not self.g.adj(s): return
        adjs = self.g.adj(s)
        print(f'adjs for s {s} = {adjs}')
        for w in self.g.adj(s):
            if w not in self.visited:
                self.dfs(w, t, found)
        self.visited.clear()
        return


def cut_path(matrix):
    g = Graph(grid=matrix)
    dfs = DFS(graph=g)
    m, n = len(matrix), len(matrix[0])
    if (m, n) == (1, 2) or (m, n) == (2, 1): return False
    paths = dfs.num_paths((0, 0), (m - 1, n - 1))
    if not paths or paths == 2: return False
    return True

if __name__ == '__main__':
    grid = [[1,1,0,0,0,0],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,0,1],[0,0,0,1,1,1],[0,0,0,1,0,1],[0,0,0,1,0,1],[0,0,0,1,0,1],[0,0,0,1,0,1],[0,0,0,1,1,1]]
    for line in grid:
        print(line)
    print(f'm = {len(grid)}, n = {len(grid[0])}')
    print(cut_path(grid))
    # print(cut_path([[1,1,1],[1,0,1],[1,1,1]]))