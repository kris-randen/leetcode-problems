"""



"""
from typing import List

def check(s, l, r):
    k, b = 0, s[l]
    for i in range(l, r + 1):
        if not s[i] == b + pow(-1, k): return False
        k += 1
    return True

def alternatingSubarray(nums: List[int]) -> int:
    if len(nums) < 2: return -1
    n, l, r, m, s = len(nums), 0, 1, 0, 0
    b = nums[l]; c =0
    while r < n and c < 10:
        if check(nums, l, r):
            r += 1
            m = r - l - 1; s = max(s, m)
        l = r; r += 1
        c += 1
    return s



if __name__ == '__main__':
    s1 = [2,3,4,3,4]
    s2 = [4,5,6]
    print(alternatingSubarray(s1))
    print(alternatingSubarray(s2))