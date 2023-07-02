"""
1427. Perform 08 String Shifts
Easy
214
5
company
Goldman Sachs
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [directioni, amounti]:

directioni can be 0 (for left shift) or 1 (for right shift).
amounti is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.



Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation:
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
"""

def left(s): return s[1:] + [s[0]]

def right(s): return [s[-1]] + s[:-1]

def lefts(s, k):
    for i in range(k): s = left(s)
    return s

def rights(s, k):
    for i in range(k): s = right(s)
    return s

def shifted(s, shifts):
    l = list(s)
    for shift in shifts:
        if shift[0] == 0: l = lefts(l, shift[1])
        else: l = rights(l, shift[1])
    return ''.join(l)