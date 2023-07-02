"""
64. Minimum Path Sum
Medium
11K
139
company
Amazon
company
Apple
company
Google
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""

"""
You can only reach the bottom right from two places
1. m - 2, n - 1  (indices)
2. m - 1, n - 2  (indices)

So path(m + 1, n + 1) = min(path(m, n + 1), path(m + 1, n)) + grid[m][n]

path(1, 1) = grid[0][0]
path(2, 1) = path(1, 1) + grid[1][0]
...
...
path(m, 1) = path(m - 1, 1) + grid[m - 1][0]

path(1, 2) = path(1, 1) + grid[0][1]
...
...
path(1, n) = path(1, n - 1) + grid[0][n - 1]

path(2, 2) = min(path(1, 2), path(2, 1)) + grid[1][1]
path(3, 2) = min(path(2, 2), path(3, 1)) + grid[2][1]
...
...
path(m, 2) = min(path(m - 1, 2), path(m, 1)) + grid[m - 1][1]
"""


def min_path_sum(grid):
    if not grid: return 0
    m, n = len(grid), len(grid[0])
    sum_grid = [[0 for i in range(n)] for j in range(m)]
    sum_grid[0][0] = grid[0][0]

    for row in range(1, m):
        sum_grid[row][0] = sum_grid[row - 1][0] + grid[row][0]
    for col in range(1, n):
        sum_grid[0][col] = sum_grid[0][col - 1] + grid[0][col]

    for row in range(1, m):
        for col in range(1, n):
            sum_grid[row][col] = min(sum_grid[row - 1][col], sum_grid[row][col - 1]) + grid[row][col]

    return sum_grid[m - 1][n - 1]

def min_path_sum_small(grid):
    if not grid: return 0
    m, n = len(grid), len(grid[0])
    sum_grid_prev = [0 for i in range(n)]
    sum_grid_next = [0 for i in range(n)]
    sum_grid_prev[0] = grid[0][0]

    for col in range(1, n):
        sum_grid_prev[col] = sum_grid_prev[col - 1] + grid[0][col]

    for row in range(1, m):
        sum_grid_next[0] = sum_grid_prev[0] + grid[row][0]
        for col in range(1, n):
            sum_grid_next[col] = min(sum_grid_prev[col], sum_grid_next[col - 1]) + grid[row][col]
        sum_grid_prev = sum_grid_next

    return sum_grid_next[n - 1] if m > 1 else sum_grid_prev[n - 1]

if __name__ == '__main__':
    print(min_path_sum([[1,3,1],[1,5,1],[4,2,1]]))
    print(min_path_sum_small([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))