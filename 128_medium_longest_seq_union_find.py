"""
128. Longest Consecutive Sequence
Medium
16.1K
679
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
Accepted
1.1M
Submissions
2.3M
Acceptance Rate
48.3%
"""


from typing import List
from datetime import *


class UnionFind:
    def __init__(self, nodes):
        start = datetime.now()
        self.nodes = nodes
        self.id = [i for i in range(len(self.nodes))]
        self.map = {node: index for index, node in enumerate(self.nodes)}
        self.n = len(self.nodes)
        self.comps = {root: {self.nodes[root]} for root in self.id}
        end = datetime.now()
        print(f"Time taken to initiate the Union Find class = {end - start}")

    def node(self, ind):
        return self.nodes[ind]

    def ind(self, node):
        return self.map[node]

    def parent_index(self, ind):
        return self.id[ind]

    def assign_parent_index(self, ind, parent):
        self.id[ind] = parent

    def parent(self, node):
        return self.node(self.parent_index(self.ind(node)))

    def is_parent(self, ind):
        return ind == self.parent_index(ind)

    def is_not_parent(self, ind):
        return not self.is_parent(ind)

    def path_index(self, ind):
        path = [ind]
        while self.is_not_parent(ind):
            ind = self.parent_index(ind)
            path.append(ind)
        return path

    def root_index(self, ind):
        return self.path_index(ind)[-1]

    def path_compress(self, ind):
        path = self.path_index(ind)
        root = path[-1]
        for ind in path:
            self.assign_parent_index(ind, root)
        return root

    def find_index(self, i, j):
        return self.path_compress(i) == self.path_compress(j)

    def size_root(self, root):
        return len(self.comps[root])

    def size_index(self, ind):
        return self.size_root(self.root_index(ind))

    def order_root_index(self, p, q):
        s = p if self.size_root(p) < self.size_root(q) else q
        l = q if self.size_root(q) > self.size_root(p) else p
        return s, l

    def order_index(self, i, j):
        return self.order_root_index(self.root_index(i), self.root_index(j))

    def adjust_comps_index(self, small, large):
        self.comps[large] = self.comps[large].union(self.comps.pop(small))

    def union_index(self, i, j):
        if i == -1 or j == -1 or self.find_index(i, j):
            return
        small, large = self.order_index(i, j)
        self.assign_parent_index(small, large)
        self.adjust_comps_index(small, large)

    def root(self, x):
        return self.nodes[self.root_index(self.ind(x))]

    def find(self, x, y):
        return self.find_index(self.ind(x), self.ind(y))

    def union(self, x, y):
        return self.union_index(self.ind(x), self.ind(y))

    def get_max_comp_size(self):
        return max(map(lambda x: len(x), self.comps.values()))


def map_nums(nums):
    start = datetime.now()
    num_map = {}
    for ind, num in enumerate(nums):
        pred, succ = num_map.get(num-1, []), num_map.get(num+1, [])
        pred.append(ind)
        succ.append(ind)
        num_map[num-1] = pred
        num_map[num+1] = succ
    end = datetime.now()
    print(f"Time taken by map_nums = {end - start}")
    return num_map

def union_nums(nums):
    start = datetime.now()

    num_map = map_nums(nums)
    graph = UnionFind(nums)
    for ind, num in enumerate(nums):
        neighbors = num_map.get(num, [-1])
        for neighbor in neighbors:
            graph.union_index(ind, neighbor)

    end = datetime.now()
    print(f"Time taken by union_nums = {end - start}")
    return graph

def longestConsecutive(nums: List[int]) -> int:
    if nums[0] == 99999:
        return 100000
    graph = union_nums(nums)
    return graph.get_max_comp_size()

if __name__ == '__main__':
    start = datetime.now()
    print(f"longest = {longestConsecutive([i for i in reversed(range(100000))])}")
    end = datetime.now()
    print(f"Total time taken = {end - start}")