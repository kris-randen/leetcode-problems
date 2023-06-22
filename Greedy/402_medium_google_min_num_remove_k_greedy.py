"""
402. Remove K Digits
Medium
7.7K
327
company
PhonePe
company
Amazon
company
Uber
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.



Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

"""

"""
Idea is to remove peak digits as you find them. At the end of this operation you either have an empty stack or an increasing sequence of numbers in the stack. If we removed c peaks and c < k then we need to truncate the last k - c digits from this stack. Also remove leading zeroes before returning the final number
"""

def trim(digits):
    if not digits: return "0"
    i, n = 0, len(digits)
    while i < n and digits[i] == 0: i += 1
    return "0" if i == n else digits[i:]

def trunc(s):
    if not s: return "0"
    i, n = 0, len(s)
    while i < n and s[i] == "0": i += 1
    return "0" if i == n else s[i:]


def k_digits(num, k):
    if not num or k >= len(num): return "0"
    s, c, i, n = [], 0, 0, len(num)
    digits = list(map(int, list(num)))
    while i < n:
        if s and digits[i] < s[-1] and c < k:
            s.pop(); c += 1; continue
        s.append(digits[i]); i += 1
    return "".join(map(str, trim(s[:len(s) - (k - c)])))

def k_digits_str(num, k):
    if not num or k >= len(num): return "0"
    s, c, i, n = "", 0, 0, len(num)
    while i < n:
        if s and num[i] < s[-1] and c < k:
            s = s[:-1]; c += 1; continue
        s += num[i]; i += 1
    return trunc(s[:len(s) - (k - c)])

if __name__ == '__main__':
    s = '1234'
    print(s[1:7])