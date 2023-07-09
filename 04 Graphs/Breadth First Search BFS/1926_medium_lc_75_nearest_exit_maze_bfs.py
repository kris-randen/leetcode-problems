"""

1926. Nearest Exit from Entrance in Maze
Medium
1.9K
67
Companies
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.



Example 1:


Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.
Example 2:


Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.
Example 3:


Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.

"""

def valid_ind(m, n, i, j):
    return 0 <= i < m and 0 <= j < n

def wall(b, p):
    return b[p[0]][p[1]] == '+'

def valid(b, p):
    m, n, i, j = len(b), len(b[0]), p[0], p[1]
    return valid_ind(m, n, i, j) and not wall(b, p) and not visited(b, p)

def right(p): return p[0], p[1] + 1

def left(p): return p[0], p[1] - 1

def bottom(p): return p[0] + 1, p[1]

def top(p): return p[0] - 1, p[1]

def visited(b, p): return b[p[0]][p[1]] == '%'

def nbs(b, p): return filter(lambda p: valid(b, p), [left(p), top(p), right(p), bottom(p)])

def is_bdry_ind(m, n, i, j):
    return i == 0 or j == 0 or i == m - 1 or j == n - 1

def is_bdry(b, p):
    return is_bdry_ind(len(b), len(b[0]), p[0], p[1])

def is_exit(b, p, e):
    return p != e and is_bdry(b, p) and not wall(b, p)

def mark(b, p): b[p[0]][p[1]] = '%'

def nearest(b, e):
    m, n = len(b), len(b[0])
    if not b: return 0
    q, c = [[e]], 0
    while q:
        ps, cs = q.pop(), []
        for p in ps:
            if visited(b, p): continue
            if is_exit(b, p, e): return c
            mark(b, p)
            cs += nbs(b, p)
        c += 1
        if cs: q.append(cs)
    return -1

if __name__ == '__main__':
    print('hello')

