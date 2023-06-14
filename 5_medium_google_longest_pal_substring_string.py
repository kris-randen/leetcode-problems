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

# There are 2n - 1 centers for palindromes in any string of length n
# From each center starting from the middle center we start going out
# we find the longest palindrome and recurse on the left and right
# halves.

def index(c):
    return [c//2, c//2 + 1] if (c + 1) % 2 == 0 else [c//2]

def update_start_max(start_max, index, length):
    start, max_length = start_max
    if length > max_length: start_max[0], start_max[1] = index, length

def max_palindrome(s):
    n = len(s)
    if n < 2: return s
    centers = [_ for _ in range(2*n - 1)]
    start_max_length = [0, 1]

    for center in centers: centred_palindrome(s, center, start_max_length)
    start, max_length = start_max_length
    return s[start:start + max_length]

def centred_palindrome(s, c, start_max):
    i, n, indices, even, radius = 0, len(s), index(c), (c + 1) % 2 == 0, start_max[1] // 2
    l, r = (indices[0], indices[1]) if even else (indices[0], indices[0])
    if l - radius < 0 or r + radius > n - 1: return
    while l - i >= 0 and r + i < n and s[l - i] == s[r + i]:
        length = (2 * i + 1) if not even else 2*(i + 1)
        update_start_max(start_max, l - i, length)
        i += 1


if __name__ == '__main__':
    print(max_palindrome("babad"))