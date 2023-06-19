"""
740. Delete and Earn
Medium
6.6K
335
company
Bloomberg
company
Amazon
company
Goldman Sachs
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.



Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
"""
from functools import reduce

"""
earn(v):
  earning, collected, deleted
  
collect(v, a):
  return v - {a}, v - {a + 1, a - 1}

earn(n + 1) = earn(n) + v[n] if v[n] in earn(n).collected
            = earn(n) + v[n] if v[n] not in collected and not in deleted
            = max(earn(collect(v, v[n]) + v[n])), earn(n))
            
[2,2,3,3,3,4]

[2, 3, 4]

[] - 2 - [2] = 2
[2] - 3 - part of deleted so... [2, 3] collect 3 - [] 3 + 0, 2 max = 3
[2, 3, 4] - 4 is part of deleted so ... [2, 3, 4] collect 4 - [2] - earn 2 = 6, 3 max 6
[2, 3, 4, 3] - 3 is part of deleted so ... [2, 3, 3, 4] collect 3 - 3 + earn [3] = 6, delete 3 = 6 max 6
[2, 3, 3, 4] - 3 is part of deleted [2, 3, 3, 3, 4] collect 3 - [3, 3] - 9
"""

def max_list(v):
    return 0 if not v else max(v)

def map_list(v):
    mapped = {}
    for val in v:
        if val in mapped:
            mapped[val] += val
        else:
            mapped[val] = val
    return mapped

def robber_list(m):
    keys = m.keys().sorted()
    gold = []
    for key in keys:
        gold.append(m[key])
        if key + 1 not in keys:
            gold.append(0)
    return gold

def max_robbery(r):
    if len(r) < 3: return max_list(r)
    robbed = [r[0], max(r[0], r[1])]
    for i in range(2, len(r)):
        robbed[i] = max(robbed[i - 1], robbed[i - 2] + r[i])
    return robbed[-1]

def earn(v):
    return max_robbery(robber_list(v))



if __name__ == '__main__':
    v = []
    print(max_list(v))
