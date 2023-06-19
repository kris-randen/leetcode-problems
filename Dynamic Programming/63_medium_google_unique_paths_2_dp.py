"""
63. Unique Paths II
Medium
7.1K
441
Cruise Automation
company
Amazon
company
Google
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
"""

"""
Let's try and reduce this to min path sum (problem 64) that we just solved. 

Notice that if we have 0s for spaces and 1s for obstacles we'll find the min sum path by avoiding 1s.

But instead of adding path sums we just need to add the number of paths.

Again to reach cell[m][n] the only two ways are from cell[m - 1][n] and down or cell[m][n - 1] and right.

Now everytime we're trying to find the paths we'll check which one is the minimum of the two.

If only one of them is the min say [m][n - 1] then the number of paths to [m][n] = paths[m][n - 1]

and if both are equal paths[m][n] = paths[m][n - 1] + paths[m - 1][n]

So paths[0][0] = paths[0][1] = ... = paths[0][n - 1] = 1
likewise
paths[0][0] = paths[1][0] = ... = paths[m - 1][0] = 1


if the single row or col has an obstacle then we have one path leading up to the cell before that and zero afterwards.

paths[1][1] = paths[0][1] + paths[1][0]


paths[1][2] = paths[0][2] + paths[1][1]
"""

def num_paths(grid):
    if not grid: return 0
    m, n = len(grid), len(grid[0])
    paths_prev = [0 for _ in range(n)]
    paths_next = [0 for _ in range(n)]

    paths_prev[0] = 1 if grid[0][0] == 0 else 0
    if m == 1 and n == 1: return paths_prev[0]
    for col in range(1, n):
        paths_prev[col] = paths_prev[col - 1] if grid[0][col] == 0 else 0

    if m == 1: return paths_prev[n - 1]

    paths_next[0] = paths_prev[0] if grid[1][0] == 0 else 0

    for row in range(1, m):
        paths_next[0] = paths_prev[0] if grid[row][0] == 0 else 0

        for col in range(1, n):
            paths_next[col] = paths_prev[col] + paths_next[col - 1] if grid[row][col] == 0 else 0
        paths_prev = paths_next

    return paths_next[n - 1]

if __name__ == '__main__':
    u = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,1],[0,0],[0,0],[1,0],[0,0],[0,0],[0,1],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,1],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0]]

    for line in u:
        print(line)
    print(num_paths(u))