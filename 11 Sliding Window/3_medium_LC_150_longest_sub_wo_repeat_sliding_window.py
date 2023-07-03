"""
3. Longest Substring Without Repeating Characters
Medium
35.1K
1.6K
Companies
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

"""



"""

def longest(s):
    if len(s) < 2: return len(s)
    n, l, r, w, seen = len(s), 0, 0, 0, {}
    for r in range(n):
        c = s[r]
        if c in seen and seen[c] >= l:
            l = seen[c] + 1
        w = max(w, r - l + 1); seen[c] = r
    return w