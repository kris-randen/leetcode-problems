"""
209. Minimum Size Subarray Sum
Medium
9.7K
278
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

"""

"""
Explanation: Python Sliding Window 8 lines - O(n) 99.4 %-ile solution

Intuition
Sliding Window
You slide the right of your window while sum is less than target and the left side while the sum is greater than equal to target.

Approach
Sliding Window
You slide the right of your window while sum is less than target and the left side while the sum is greater than equal to target.

We start with an initial width of n + 1 (float('inf') works but is slightly less performant).

You start with your left and right window pointers at 0 and -1. I do this instead of starting both at 0 so that I can start my sum s at 0 instead of v[0] again for slight perforrmance boost.

Now our while loop can't just check for r < n because that misses the corner cases of when you have hit the right most end of the array with r and now the sum goes below target.

Your naive while loop will again increment r and you'll go out of bounds. For this you can either have an if statement inside and break but that's not my personal preference.

Complexity
Time complexity:
O(n): You can through the complete array once in the worst case with both l and r pointers.

Space complexity:
O(1): We only maintain a few variales like sum (s), min sub array size (w), l, r and array length n.

"""

def min_sub_size_sum(v, t):
    if not v: return 0
    n, l, r, s = len(v), 0, -1, 0; w = n + 1
    while r < n and (s >= t or r < n - 1):
        if s < t:
            r += 1; s += v[r]
        else:
            w = min(w, r - l + 1)
            s -= v[l]; l += 1
    return w if w < n + 1 else 0












