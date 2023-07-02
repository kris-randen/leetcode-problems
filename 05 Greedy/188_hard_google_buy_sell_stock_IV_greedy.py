"""
188. Best Time to Buy and Sell Stock IV
Hard
6.5K
195
company
Amazon
company
Bloomberg
company
Google
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

"""
import heapq

"""

THIS REDUCTION IS INCORRECT

This problem can be reduced to keeping track of the k max items seen so far in a stream of items. The way it reduces is the following: recored all buy and sell prices bi, si so far. Among these we need to select the k highest profit transactions.

The solution to k max items is as follows:

Maintain a min heap of size k. For the first k items push each item into the heap. For every k + 1 th item and higher check if it's greater or smaller than the top / min element in the heap. If it is less than or equal to min let it go. If it is greater then pop the min and push this item on to the heap.

Identifying buy sell prices / profits reduces to Problem 122 Buy Sell Stock II. 

The above reduction is wrong.

The right 03 Dynamic Programming approach is as follows:

Let's consider dp[j, k] as the max profit with at most k transactions at the end of day n.

There are two possibilities in the optimal solution:

1. A sale / transaction does not happen at day j

In this case dp[j, k] = dp[j - 1, k]

2. A sale / transaction does happen at day j

In this case let the day this last transaction's buy happened
be i. Since you can have only one transaction open at one time

In this case dp[j, k] = p[j] - p[i] + dp[i - 1, k - 1]

We need to consider all possible combinations for case 2 so

i goes from 0 to j - 1

Therefore dp[j, k] = max(dp[j - 1, k], {p[j] - p[i] + dp[i - 1, k - 1] for i-> (0, j -1)}

We can also observe that if the price at day j aka p[j] <= p[j - 1] a sale can't happen at day j in the optimal case. So in this case we can eliminate computing the second sub cases.

dp[0, k] = 0 for all k
dp[1, k] = max(0, p[1] - p[0])

Also note that for j <= 2k we can just take all buy-sells and add them up it's only for j > 2k we need to worry about optimizing. Because for j <= 2k no matter what we can't have more than k transactions any way. The most buy sells we could have in 2k days is k.

dp[0, k] = 0 for all k
dp[1, k] = max(dp[0, k], {p[1] - p[0]}
dp[2, k] = max(dp[1, k], {p[2] - p[1] + dp[0, k - 1], p[2] - p[0]}
dp[3, k] = max(dp[2, k], {p[3] - p[2] + dp[1, k - 1]
"""

def buy_sell(prices):
    if not prices: return 0
    n, bi, si, l_min, l_max, p = len(prices), 0, 0, float('inf'), float('-inf'), []
    for i in range(1, n):
        if prices[i] <= prices[i - 1]:
            #close the transaction and reset buy sell days
            p.append(prices[si] - prices[bi]); si = bi = i

        if prices[i] > prices[i - 1]:
            # increment the day for selling
            si += 1

            # but if you reach the end of all days close it again
            if i == n - 1: p.append(prices[si] - prices[bi])
    return p

def max_k_items(items, k):
    max_k, count = [float('inf')] * k, 0
    heapq.heapify(max_k)
    for item in items:
        if count < k:
            heapq.heappush(items, item); count += 1; continue
        if item <= max_k[0]: continue
        heapq.heapreplace(max_k, item)
    return max_k

def max_profit_k(prices, k):
    p, max_k = 0, max_k_items(buy_sell(prices), k)
    while max_k:
        p += heapq.heappop(max_k)
    return p