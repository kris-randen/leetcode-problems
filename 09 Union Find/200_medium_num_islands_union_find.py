from typing import List

class UnionFind:
    def __init__(self, n, count=None):
        self.id = [i for i in range(n)]
        self.sz = [1 for i in range(n)]
        self.size = n
        self.count = n if count is None else count

    def root(self, i):
        nodes = [i]
        while i != self.id[i]:
            i = self.id[i]
            nodes.append(i)
        for node in nodes:
            self.id[node] = i
        return i

    def connected(self, i, j):
        return self.root(i) == self.root(j)

    def union(self, i, j):
        if self.connected(i, j):
            return

        p = self.root(i)
        q = self.root(j)

        if self.sz[p] < self.sz[q]:
            self.id[p] = q
            self.sz[q] += self.sz[p]
        else:
            self.id[q] = p
            self.sz[p] += self.sz[q]

        self.count -= 1

    def description(self):
        desc = []
        for i in range(self.size):
            s = f"{i}"
            while i != self.id[i]:
                i = self.id[i]
                s += f" -> {i}"
            desc.append(s)
        return desc

    def print_uf(self):
        for s in self.description():
            print(s)


class Solution:
    def lin_ind(self, point, rows, cols):
        return point[0] * cols + point[1] - 1

    def neighbors(self, i, j, rows, cols):
        return filter(lambda x: 0 <= x[0] < rows and 0 <= x[1] < cols, [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])

    def grid_value(self, grid, point):
        return grid[point[0]][point[1]]

    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(rows * cols, count=0)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "0":
                    continue
                uf.count += 1
                adjacents = self.neighbors(row, col, rows, cols)
                point = (row, col)
                point_uf = self.lin_ind(point, rows, cols)
                for adjacent in adjacents:
                    if self.grid_value(grid, adjacent) == "1":
                        adj_uf = self.lin_ind(adjacent, rows, cols)
                        uf.union(point_uf, adj_uf)
        return uf.count

if __name__ == '__main__':
    uf = UnionFind(10)
    uf.union(4, 3)
    uf.union(3, 8)
    uf.union(6, 5)
    uf.union(9, 4)
    uf.union(2, 1)
    uf.union(5, 0)
    uf.union(7, 2)
    uf.union(6, 1)
    uf.union(7, 3)
    print(uf.connected(7, 3))
    print(uf.connected(8, 9))
    uf.print_uf()