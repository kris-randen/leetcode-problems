"""
274. H-Index
Medium
308
82
Companies
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.



Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1

"""

def h_index(cs):
    cs.sort(reverse=True)
    n = len(cs); l, h = 0, n - 1; m = 0
    while l < h:
        m = (l + h) // 2
        print(f'l = {l}, h = {h}, m = {m}')
        if cs[m] == m + 1:
            print('True')
            return cs[m]
        if cs[m] < m + 1:
            h = m
        else:
            l = m + 1
    return cs[l]

if __name__ == '__main__':
    print(h_index([1,3,1]))
    # print(h_index([3, 0, 6, 1, 5]))
    # u = [3, 0, 6, 1, 5]
    # us = sorted(u, reverse=True)
    # print(us)
    # v = [i < j for i, j in enumerate(us)]
    # print(v)
    # [3, 0, 6, 1, 5]
    # [1, 3, 1]

    # [1,  1,  3]
    # l, h, m = 0, 2, 1; cs[m] = 1; n - m = 2
    # l = 1; h = 2; m = 1; cs[m] = 1; n - m = 2
    #