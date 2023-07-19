"""

279. Perfect Squares
Medium
9.7K
409
Companies
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.



Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

"""

"""

Note that this problem can be reduced to the coin change problem. The denominations of the coin are all the perfect squares that could potentially sum to n. So we need to identify perfect squares for all m <= ceil(sqrt(n)) and then reduce it to the coin change problem.

"""

from math import sqrt

def coin_change(t, cs):
    if t < cs[0]: return []
    dp = [(0 if i < cs[0] else float('inf')) for i in range(t + 1)]
    dp[cs[0]] = 1
    for j in range(cs[0] + 1, t + 1):
        i = 0
        while i < len(cs) and cs[i] <= t:
            dp[j] = min(dp[j], 1 + dp[j - cs[i]]); i += 1
    return dp

class Solution:
    def __init__(self):
        self.sqs = [1]

    def find(self, n):
        s = self.sqs[-1]; m = int(sqrt(s)) + 1
        if m ** 2 > n: return self.sqs
        while m ** 2 <= n:
            self.sqs.append(m ** 2); m += 1

    def numSquares(self, n: int) -> int:
        self.find(n); dp = coin_change(n, self.sqs)
        return dp[n]

if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(13))
