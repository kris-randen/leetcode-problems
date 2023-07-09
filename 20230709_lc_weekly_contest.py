"""


"""


""""

6919. Apply Operations to Make All Array Elements Equal to Zero
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Medium
You are given a 0-indexed integer array nums and a positive integer k.

You can apply the following operation on the array any number of times:

Choose any subarray of size k from the array and decrease all its elements by 1.
Return true if you can make all the array elements equal to 0, or false otherwise.

A subarray is a contiguous non-empty part of an array.



Example 1:

Input: nums = [2,2,3,1,1,0], k = 3
Output: true
Explanation: We can do the following operations:
- Choose the subarray [2,2,3]. The resulting array will be nums = [1,1,2,1,1,0].
- Choose the subarray [2,1,1]. The resulting array will be nums = [1,1,1,0,0,0].
- Choose the subarray [1,1,1]. The resulting array will be nums = [0,0,0,0,0,0].
Example 2:

Input: nums = [1,3,1,1], k = 2
Output: false
Explanation: It is not possible to make all the array elements equal to 0.

"""























"""

6912. Longest Non-decreasing Subarray From Two Arrays
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Medium
You are given two 0-indexed integer arrays nums1 and nums2 of length n.

Let's define another 0-indexed integer array, nums3, of length n. For each index i in the range [0, n - 1], you can assign either nums1[i] or nums2[i] to nums3[i].

Your task is to maximize the length of the longest non-decreasing subarray in nums3 by choosing its values optimally.

Return an integer representing the length of the longest non-decreasing subarray in nums3.

Note: A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums1 = [2,3,1], nums2 = [1,2,1]
Output: 2
Explanation: One way to construct nums3 is: 
nums3 = [nums1[0], nums2[1], nums2[2]] => [2,2,1]. 
The subarray starting from index 0 and ending at index 1, [2,2], forms a non-decreasing subarray of length 2. 
We can show that 2 is the maximum achievable length.
Example 2:

Input: nums1 = [1,3,2,1], nums2 = [2,2,3,4]
Output: 4
Explanation: One way to construct nums3 is: 
nums3 = [nums1[0], nums2[1], nums2[2], nums2[3]] => [1,2,3,4]. 
The entire array forms a non-decreasing subarray of length 4, making it the maximum achievable length.
Example 3:

Input: nums1 = [1,1], nums2 = [2,2]
Output: 2
Explanation: One way to construct nums3 is: 
nums3 = [nums1[0], nums1[1]] => [1,1]. 
The entire array forms a non-decreasing subarray of length 2, making it the maximum achievable length.

"""

def len_nondec(v):
    if len(v) < 2: return len(v)
    n, l, r, w, lw, rw = len(v), 0, 1, 1, 0, 0
    while r < n:
        if v[r] >= v[r - 1]:
            w = max(w, r - l + 1)
            lw = l; rw = r
            r += 1
        else: l = r; r += 1
    return l

def longest_nondec(u, v):
    if len(u) < 2: return u
    agg = [min(u[0], v[0])]
    for i in range(1, len(u)):
        w, x = min(u[i], v[i]), max(u[i], v[i])
        if u[i] == agg[-1] or v[i] == agg[-1]:
            agg.append(agg[-1])
        elif x < agg[-1] or w >= agg[-1]:
            agg.append(w)
        else:
            agg.append(x)
    return agg

def long_non_dec_all(u, v):
    agg, w = [], 0
    for i in range(len(u)-1):
        for j in range(i + 1, len(u)):
            if agg and min(u[j], v[j]) >= agg[-1]:
                print(f'special case i = {i}, j = {j}, agg[-1] = {agg[-1]}')
                w += 1; continue
            agg = longest_nondec(u[i:j + 1], v[i:j + 1])
            w = max(w, len_nondec(agg))
            print(f'u = {u}, v = {v}, i = {i}, j = {j}, agg = {agg}, w = {w}')
    return w


"""

6899. Maximum Number of Jumps to Reach the Last Index
User Accepted:6294
User Tried:11236
Total Accepted:6412
Total Submissions:27114
Difficulty:Medium
You are given a 0-indexed array nums of n integers and an integer target.

You are initially positioned at index 0. In one step, you can jump from index i to any index j such that:

0 <= i < j < n
-target <= nums[j] - nums[i] <= target
Return the maximum number of jumps you can make to reach index n - 1.

If there is no way to reach index n - 1, return -1.

 

Example 1:

Input: nums = [1,3,6,4,1,2], target = 2
Output: 3
Explanation: To go from index 0 to index n - 1 with the maximum number of jumps, you can perform the following jumping sequence:
- Jump from index 0 to index 1. 
- Jump from index 1 to index 3.
- Jump from index 3 to index 5.
It can be proven that there is no other jumping sequence that goes from 0 to n - 1 with more than 3 jumps. Hence, the answer is 3. 
Example 2:

Input: nums = [1,3,6,4,1,2], target = 3
Output: 5
Explanation: To go from index 0 to index n - 1 with the maximum number of jumps, you can perform the following jumping sequence:
- Jump from index 0 to index 1.
- Jump from index 1 to index 2.
- Jump from index 2 to index 3.
- Jump from index 3 to index 4.
- Jump from index 4 to index 5.
It can be proven that there is no other jumping sequence that goes from 0 to n - 1 with more than 5 jumps. Hence, the answer is 5. 
Example 3:

Input: nums = [1,3,6,4,1,2], target = 0
Output: -1
Explanation: It can be proven that there is no jumping sequence that goes from 0 to n - 1. Hence, the answer is -1. 

"""

def within_gap(v, i, j, t):
    return abs(v[j] - v[i]) <= t


def max_jumps(v, t):
    print(f'v = {v}, t = {t}')
    if len(v) < 2: return 0
    n, l, r, jumps = len(v), 0, 1, 0
    while r < n:
        if not within_gap(v, r, l, t):
            print(f'not within gap l = {l}, r = {r}, jumps = {jumps}')
            r += 1
        else:
            print(f'within gap l = {l}, r = {r}, jumps = {jumps}')
            l = r
            r += 1
            jumps += 1
    return jumps if l == n - 1 else -1





"""

6451. Find the Maximum Achievable Number
User Accepted:13622
User Tried:14059
Total Accepted:14151
Total Submissions:16364
Difficulty:Easy
You are given two integers, num and t.

An integer x is called achievable if it can become equal to num after applying the following operation no more than t times:

Increase or decrease x by 1, and simultaneously increase or decrease num by 1.
Return the maximum possible achievable number. It can be proven that there exists at least one achievable number.

 

Example 1:

Input: num = 4, t = 1
Output: 6
Explanation: The maximum achievable number is x = 6; it can become equal to num after performing this operation:
1- Decrease x by 1, and increase num by 1. Now, x = 5 and num = 5. 
It can be proven that there is no achievable number larger than 6.

Example 2:

Input: num = 3, t = 2
Output: 7
Explanation: The maximum achievable number is x = 7; after performing these operations, x will equal num: 
1- Decrease x by 1, and increase num by 1. Now, x = 6 and num = 4.
2- Decrease x by 1, and increase num by 1. Now, x = 5 and num = 5.
It can be proven that there is no achievable number larger than 7.

"""

def max_achievable(num, t):
    return num + 2*t


def maxNonDecreasingLength(nums1, nums2):
    n = len(nums1)
    dp1 = [1] * n
    dp2 = [1] * n
    max_len = 1

    for i in range(1, n):
        if nums1[i] >= nums1[i-1]:
            dp1[i] = dp1[i-1] + 1
        if nums2[i] >= nums2[i-1]:
            dp2[i] = dp2[i-1] + 1
        if nums1[i] >= nums2[i-1]:
            dp2[i] = max(dp2[i], dp1[i-1] + 1)
        if nums2[i] >= nums1[i-1]:
            dp1[i] = max(dp1[i], dp2[i-1] + 1)

        max_len = max(max_len, dp1[i], dp2[i])

    return max_len






if __name__ == '__main__':
    # u = [8, 7, 4]
    # v = [13, 4, 4]
    # u1 = [2, 3, 1]
    # v1 = [1, 2, 1]
    # u2 = [1, 3, 2, 1]
    # v2 = [2, 2, 3, 4]
    # u3 = [1, 1]
    # v3 = [2, 2]
    # u4 = [11, 7, 7, 9]
    # v4 = [19, 19, 1, 7]
    # u5 = [12, 10]
    # v5 = [16, 2]
    # u6 = [2, 3, 1]
    # v6 = [1, 2, 1]
    # print(longest_nondec(u, v))
    # print(longest_nondec(u1, v1))
    # print(longest_nondec(u2, v2))
    # print(longest_nondec(u3, v3))
    # print(longest_nondec(u4, v4))

    # print(long_non_dec_all(u, v))
    # print(long_non_dec_all(u1, v1))
    # print(long_non_dec_all(u2, v2))
    # print(long_non_dec_all(u3, v3))
    # print(long_non_dec_all(u4, v4))
    # print(long_non_dec_all(u5, v5))
    # print(long_non_dec_all(u6, v6))
    #
    # print(len_nondec([12, 2]))

    v = [1, 3, 6, 4, 1, 2]
    t = 0
    v1 = [1, 0, 2]
    t1 = 1

    print(max_jumps(v, t))
    print(max_jumps(v1, t1))
    x, y = [1,8], [10,1]
    x1 = [4, 2]
    y1 = [10, 4]

    print(f'max nondec = {maxNonDecreasingLength(x1, y1)}')


