"""
55. Jump Game
Medium
16.5K
860
company
Amazon
company
Microsoft
company
Apple
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

"""

""""
dp[n] = number of steps left, last number
dp[n] = True if dp[n - 1] == 0, a != 0
      = True if dp[n - 1][0] > 0
      = False if dp[n - 1] == 0, 0 or dp[n - 1] is False
      
dp[1] = True, v[0], v[0]
dp[2] = False if v[0] = 0, v[1], v[1]

"""

def jump_game_long(steps):
    if not steps or len(steps) == 1: return True
    if steps[0] == 0: return False
    n, dp = len(steps), [(False, 0)] * len(steps); dp[0] = (True, 0)
    for i in range(1, n):
        k = dp[i - 1][1]
        valid = False if (steps[k] == (i - 1 - k) and steps[i - 1] == 0) or not dp[i - 1][0] else True
        remaining = steps[k] - (i - k)
        l = k if remaining >= steps[i - 1] else i - 1
        dp[i] = valid, l
    print(f'dp {dp}')
    return dp[-1][0]

def jump_game(steps):
    m = 0
    for i in range(len(steps)):
        if i > m: return False
        m = max(m, i + steps[i])
    return True