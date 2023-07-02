"""
1277. Count Square Submatrices with All Ones
Medium
4.3K
71
company
Google
company
Amazon
company
Microsoft
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.



Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.

"""

def count_1s(m):
    count = 0
    if m is None: return count
    for line in m:
        for point in line:
            count += point
    return count

def check(m, i, j):
    return m[i][j] == 1 and m[i + 1][j] == 1 and \
           m[i][j + 1] == 1 and m[i + 1][j + 1] == 1

def shrink(u):
    h, w = len(u), len(u[0])
    if min(h, w) <= 1:
        return None
    shrunk = [[0 for _ in range(w - 1)] for _ in range(h - 1)]
    for row in range(h - 1):
        for col in range(w - 1):
            shrunk[row][col] = 1 if check(u, row, col) else 0
    return shrunk

def count_all(u):
    count, c = 0, count_1s(u)
    h, w = len(u), len(u[0])
    if min(h, w) <= 1:
        return count
    while c >= 1:
        count += c
        u = shrink(u)
        c = count_1s(u)
    return count

if __name__ == '__main__':
    print(count_all([[1,0,1],[1,1,0],[1,1,0]]))