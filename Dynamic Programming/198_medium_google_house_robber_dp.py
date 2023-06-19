"""
198. House Robber
Medium
18K
341
company
Cisco
company
Amazon
company
Google
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""

def max_loot(sums):
    if not sums:
        return 0
    if len(sums) == 1:
        return sums[0]
    if len(sums) == 2:
        return max(sums[0], sums[1])

    n = len(sums)
    loot = []
    loot[0] = sums[0]
    loot[1] = max(sums[0], sums[1])

    for i in range(3, n):
        loot[i] = max(loot[i - 1], loot[i - 2] + sums[i])

    return loot[n - 1]

