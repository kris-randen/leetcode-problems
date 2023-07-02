"""
624. Maximum Distance in Arrays
Medium
669
66
company
Yahoo
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.



Example 1:

Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Example 2:

Input: arrays = [[1],[1]]
Output: 0

"""
from typing import List


def min_vss(vss, skip=None):
    min_vs, min_i = float('inf'), -1
    for i, vs in enumerate(vss):
        if skip is not None and i == skip: continue
        if min_vs > vs[0]: min_vs = vs[0]; min_i = i
    return min_i, min_vs


def max_vss(vss, skip=None):
    max_vs, max_i = float('-inf'), -1
    for i, vs in enumerate(vss):
        if skip is not None and i == skip: continue
        if max_vs < vs[-1]: max_vs = vs[-1]; max_i = i
    return max_i, max_vs


def sort_vss(vss, skip=None, reverse=False):
    os, oi = float('inf') if not reverse else float('-inf'), -1
    for i, vs in enumerate(vss):
        if skip is not None and i == skip: continue
        if not reverse:
            if os > vs[0]: os = vs[0]; oi = i
        else:
            if os < vs[-1]: os = vs[-1]; oi = i
    return oi, os

# Using separate min and max functions instead of a generic sort gives far better performance


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        if not arrays: return 0
        min_i, min_vs = min_vss(arrays)
        max_i, max_vs = max_vss(arrays)
        min_max_a = abs(max_vs - min_vs)
        l, h = min_vs, max_vs
        if min_i == max_i:
            mi = max_i
            max_i, max_vs = max_vss(arrays, skip=mi)
            min_i, min_vs = min_vss(arrays, skip=mi)
        return max(abs(max_vs - l), abs(h - min_vs))