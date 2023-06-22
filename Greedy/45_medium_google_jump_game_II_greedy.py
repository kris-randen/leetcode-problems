"""
45. Jump Game II
Medium
12.5K
435
company
Amazon
company
Bloomberg
company
Adobe
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

"""

def min_steps(steps):
    if len(steps) < 2: return 0
    i, s, n = 0, 0, len(steps)
    while i < n:
        delta = 0
        for k in range(steps[i]):
            if i + k >= n - 1: return s + 1
            delta = max(delta, k + steps[i + k])
        i += delta; s += 1
    return s


def min_steps_long(abc):
    if len(abc) < 2: return 0
    i, s, n = 0, 0, len(abc)
    print(f'n is = {n}')
    while i < n - 2:
        print(f'i {i}')
        print(f'steps[{i}]')
        print(f'{abc[i]}')
        if i + abc[i] >= n - 1:
            return s + 1
        delta = 0
        for k in range(abc[i] + 1):
            print(f'k {k}')
            if i + k >= n - 1:
                return s + 1
            delta = max(delta, k + abc[i + k])
        i += delta; s += 2
    return s

if __name__ == '__main__':
    s = [5,9,3,2,1,0,2,3,3,1,0,0]
    print(min_steps_long(s))