"""

85. Maximal Rectangle
Hard
9.3K
144
Companies
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.



Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1


Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.


"""

"""

S-i,j,k+1,l = S-i,j,k,l and S-i+k,j,1,l

S-i,j,1,1 = a-i,j
S-i,j,2,1 = S-i,j,1,1 and S-i+1,j,1,1

S-0,0,2,1 = S-0,0,1,1 and S-1,0,1,1

"""

from collections import defaultdict

def rectangles(t):
    if not t or not t[0]: return 0
    m, n = len(t), len(t[0])
    sheet, max_area = [[False] * n for _ in range(m)], 0
    rects = [[[[False] * n for _ in range(m)] for _ in range(n)] for _ in range(m)]
    # for cols in rects:
    #     for col in cols:
    #         print(col)

    # print(f'rects 0, 0, 1 = {rects[0][0][1]}')

    # print(f'rects 0, 0, 1, 4 = {rects[0][0][1][4]}')

    # print(f'size of rects = {len(rects), len(rects[0])}')
    for i in range(m):
        for j in range(n):
            if t[i][j]:
                max_area = max(max_area, 1)
                rects[i][j][0][0] = True
            else:
                rects[i][j][0][0] = False
    for i in range(m - 1):
        for j in range(n - 1):
            for k in range(2,m - i + 1):
                for l in range(1, n - j + 1):
                    print(f'i = {i}, j = {j}, k = {k}, l = {l}')
                    increased = rects[i][j][k-2][l - 1] and \
                                rects[i+k-1][j][1][l - 1]
                    if increased:
                        print(f'increased')
                        rects[i][j][k-1][l-1] = True
                        max_area = max(max_area, k * l)
                    else:
                        rects[i][j][k-1][l-1] = False
    return max_area