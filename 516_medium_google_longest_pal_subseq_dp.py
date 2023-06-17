"""
516. Longest Palindromic Subsequence
Medium
8.4K
312
company
Cisco
company
Amazon
company
LinkedIn
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

"""

"""
0  1  2  3  4  5  6  7  8
a  -  b  -  b  -  c  -  a
0     1     2     3     4
"""

def is_even(c):
    return (c + 1) % 2 == 0

def index(c):
    return [c // 2, c // 2 + 1] if is_even(c) else [c // 2]

def left_bound(s, l, il):
    return l - il > -1

def right_bound(s, r, ir):
    return r + ir < len(s)

def bounded(s, l, r, il, ir):
    return left_bound(s, l, il) and right_bound(s, r, ir)

def pal(s, l, r, il, ir):
    return s[l - il] == s[r + ir]

def bounded_non_pal(s, l, r, il, ir):
    return bounded(s, l, r, il, ir) and not pal(s, l, r, il, ir)

def right_ind(s, l, r, il, ir):
    while bounded_non_pal(s, l, r, il, ir):
        ir += 1
    return ir if right_bound(s, r, ir) else None

def left_ind(s, l, r, il, ir):
    while bounded_non_pal(s, l, r, il, ir):
        il -= 1
    return il if left_bound(s, l, il) else None


def long_pal_subseq_2D(s):
    if len(s) < 2: return len(s)

    dp = [[1 if i == j else 0 for j in range(len(s))] for i in range(len(s))]

    length = 1

    for l in range(2, len(s) + 1):
        for i in range(len(s) - l + 1):
            j = i + l - 1
            dp[i][j] = dp[i + 1][j - 1] + 2 if s[i] == s[i + l - 1] else max(dp[i][j - 1], dp[i + 1][j])
            length = max(length, dp[i][i + l - 1])
    return length


def long_pal_subseq_1D(s):
    if len(s) < 2: return len(s)

    dp_prev = [1 for _ in range(len(s))]
    dp_next = [2 if s[i] == s[i + 1] else 1 for i in range(len(s) - 1)]

    if len(s) == 2: return max(dp_next)

    dp_new = [0 for i in range(len(s) - 2)]
    length = 1

    for l in range(3, len(s) + 1):
        for i in range(len(s) - l + 1):
            j = i + l - 1
            dp_new[i] = dp_prev[i + 1] + 2 if s[i] == s[j] else max(dp_next[i], dp_next[i + 1])
            length = max(length, dp_new[i])
        dp_prev = dp_next.copy()
        dp_next = dp_new.copy()

    return length

