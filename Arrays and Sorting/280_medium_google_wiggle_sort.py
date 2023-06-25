"""
280. Wiggle Sort
Medium
1.1K
97
company
Amazon
company
Google
company
Microsoft
Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

You may assume the input array always has a valid answer.



Example 1:

Input: nums = [3,5,2,1,6,4]
Output: [3,5,1,6,2,4]
Explanation: [1,6,2,5,3,4] is also accepted.
Example 2:

Input: nums = [6,6,5,6,3,8]
Output: [6,6,5,6,3,8]

"""

def wiggle(v):
    v.sort(); n = len(v)
    if len(v) < 3: return
    for i in range(1, n - 1, 2):
        if i + 1 < n: v[i], v[i + 1] = v[i + 1], v[i]