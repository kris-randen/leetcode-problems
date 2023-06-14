"""
1641. Count Sorted Vowel Strings
Medium
3.5K
77
company
Amazon
company
Google
company
Salesforce
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.



Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Example 3:

Input: n = 33
Output: 66045

"""

# Always keep track of the number of strings that end with a, e, i, o and u
# So if t(n + 1) = a(n) * 5 + e(n) * 4 + i(n) * 3 + o(n) * 2 + u(n) * 1
# t(n + 1) = a(n + 1) + e(n + 1) + ... + u(n + 1)
# a(n + 1) = a(n)
# e(n + 1) = a(n) + e(n)
# i(n + 1) = a(n) + e(n) + i(n)
#...
#...
# u(n + 1) = a(n) + e(n) + i(n) + o(n) + u(n)
# a(n + 1) = a(n)
# e(n + 1) = a(n + 1) + e(n)
# i(n + 1) = e(n + 1) + i(n)
#...
# a(1) = e(1) = ... = u(1) = 1
# a(2) = 1, e(2) = 2, i(2) = 3, o(2) = 4, u(2) = 5

def fibonacci_nd(k, n):
    prev = [1] * (k + 1)
    prev[0] = 0
    curr = [1] * (k + 1)
    curr[0] = 0

    for i in range(1, n):
        for k in range(1, k + 1):
            curr[k] = curr[k - 1] + prev[k]
        prev = curr

    return sum(curr)

