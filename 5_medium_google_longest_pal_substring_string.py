"""
5. Longest Palindromic Substring
Medium
25.5K
1.5K
company
Amazon
company
Microsoft
company
TikTok
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

"""

def longest_palindrome(s):
    if len(s) < 2:
        return s

    n = len(s)
    start = 0
    max_len = 1

    table = [[False] * n for _ in range(n)]

    for i in range(n):
        table[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            max_len = 2
            start = i
            table[i][i + 1] = True

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and table[i + 1][j - 1]:
                max_len = length
                start = i
                table[i][j] = True

    return s[start:start + max_len]