"""
4. Median of Two Sorted Arrays
Hard
23.7K
2.7K
company
Amazon
company
Adobe
company
Google
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
Accepted
1.9M
Submissions
5.3M
Acceptance Rate
36.6%
"""

from typing import List

def median(a, b):
    m, n = len(a), len(b)
    l = m + n
    if l % 2 == 1:
        return kth(a, b, l // 2)
    else:
        return (kth(a, b, l // 2) + kth(a, b, l // 2 - 1)) / 2


def kth(a, b, k):
    if not a and not b:
        return 0
    if not a:
        return b[k]
    if not b:
        return a[k]
    ia, ib = len(a) // 2, len(b) // 2
    ma, mb = a[ia], b[ib]

    if ia + ib < k:
        if ma > mb:
            return kth(a, b[ib + 1:], k - ib - 1)
        else:
            return kth(a[ia + 1:], b, k - ia - 1)
    else:
        if ma > mb:
            return kth(a[:ia], b, k)
        else:
            return kth(a, b[:ib], k)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return 0

if __name__ == '__main__':
    u = [1, 3]
    v = [2]
