"""
309. Best Time to Buy and Sell Stock with Cooldown
Medium
8.4K
282
company
Amazon
company
Adobe
company
Bloomberg
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0

"""

def max_profit_cool_k(prices, k):
    if not prices: return 0
    n, bi, si, p, i = len(prices), 0, 0, 0, 1
    while i < n:
        if prices[i] <= prices[i - 1]:
            p += prices[si] - prices[bi]; si = bi = i
            i += k
        if prices[i] > prices[i - 1]:
            si += 1
            if i == n - 1:
                p += prices[si] - prices[bi]

    return p