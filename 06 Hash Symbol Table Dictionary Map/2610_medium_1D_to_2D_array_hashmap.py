"""

2610. Convert an Array Into a 2D Array With Conditions
Medium
364
9
Companies
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.



Example 1:

Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.
Example 2:

Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]
Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.

"""

from collections import defaultdict
from typing import List


def map_nums(ns):
    res, maxi = defaultdict(int), 0
    for i, n in enumerate(ns):
        res[n] += 1; maxi = maxi if maxi > res[n] else res[n]
    return res, maxi

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res, ind = defaultdict(list), defaultdict(int)
        for i, n in enumerate(nums):
            res[ind[n]].append(n); ind[n] += 1
        return res.values()
        # mns, maxi = map_nums(nums); res = []
        # for i in range(maxi):
        #     cs = []
        #     for mn in mns:
        #         if mns[mn]:
        #             cs.append(mn); mns[mn] -= 1
        #     res.append(cs)
        # return res