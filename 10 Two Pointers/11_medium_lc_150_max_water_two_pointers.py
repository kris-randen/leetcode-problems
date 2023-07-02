"""
11. Container With Most Water
Medium
25K
1.3K
Companies
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""

def max_water_rec(hs, l, r):
    if l >= r: return 0
    p, q = hs[l], hs[r]; a, b = p * (r - l), q * (r - l)
    if p <= q:
        return max(a, max_water_rec(hs, l + 1, r))
    else:
        return max(b, max_water_rec(hs, l, r - 1))

def max_water(hs):
    n = len(hs); l, r, area = 0, n - 1, 0
    while l <= r:
        p, q = hs[l], hs[r]
        a, b = p * (r - l), q * (r - l)
        if p <= q:
            l += 1; area = max(area, a)
        else:
            r -= 1; area = max(area, b)
    return area