"""

994. Rotting Oranges
Medium
11K
350
Companies
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

"""

def valid_ind(m, n, i, j):
    return 0 <= i < m and 0 <= j < n

def valid(b, p):
    return valid_ind(len(b), len(b[0]), p[0], p[1]) and is_fresh(b, p)

def val(b, p): return b[p[0]][p[1]]

def mark_val(b, p, val): b[p[0]][p[1]] = val

def is_rotten(b, p): return val(b, p) == 2

def is_fresh(b, p): return val(b, p) == 1

def is_empty(b, p): return val(b, p) == 0

def right(p): return p[0], p[1] + 1

def left(p): return p[0], p[1] - 1

def bottom(p): return p[0] + 1, p[1]

def top(p): return p[0] - 1, p[1]

def surr(p): return [left(p), top(p), right(p), bottom(p)]

def nbs(b, p): return filter(lambda p: valid(b, p), surr(p))

def mark(b, p, fresh):
    mark_val(b, p, 2); fresh.remove(p)

def is_val(b, p, v): return val(b, p) == v

def all_val(b, v):
    vals, m, n = set(), len(b), len(b[0])
    for i in range(m):
        for j in range(n):
            if is_val(b, (i, j), v): vals.add((i, j))
    return vals

def all_fresh(b): return all_val(b, 1)

def all_rotten(b): return all_val(b, 2)

def rotting(b):
    fresh, rotten = all_fresh(b), all_rotten(b)
    q, mins = [rotten], 0
    while q:
        ps, cs = q.pop(), set()
        for p in ps:
            if not is_rotten(b, p): mark(b, p, fresh)
            cs = cs.union(nbs(b, p))
        if not fresh: return mins
        if cs: q.append(cs); mins += 1
    return mins if not fresh else -1

if __name__ == '__main__':
    b = [[2,2],[1,1],[0,0],[2,0]]
    print(rotting(b))