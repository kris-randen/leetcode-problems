"""
1167. Minimum Cost to Connect Sticks
Medium
1.2K
152
company
Amazon
JPMorgan
company
Google
You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.

You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. You must connect all the sticks until there is only one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.



Example 1:

Input: sticks = [2,4,3]
Output: 14
Explanation: You start with sticks = [2,4,3].
1. Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4].
2. Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9].
There is only one stick left, so you are done. The total cost is 5 + 9 = 14.
Example 2:

Input: sticks = [1,8,3,5]
Output: 30
Explanation: You start with sticks = [1,8,3,5].
1. Combine sticks 1 and 3 for a cost of 1 + 3 = 4. Now you have sticks = [4,8,5].
2. Combine sticks 4 and 5 for a cost of 4 + 5 = 9. Now you have sticks = [9,8].
3. Combine sticks 9 and 8 for a cost of 9 + 8 = 17. Now you have sticks = [17].
There is only one stick left, so you are done. The total cost is 4 + 9 + 17 = 30.
Example 3:

Input: sticks = [5]
Output: 0
Explanation: There is only one stick, so you don't need to do anything. The total cost is 0.


Constraints:

1 <= sticks.length <= 104
1 <= sticks[i] <= 104
Accepted
105.1K
Submissions
153.2K
Acceptance Rate
68.6%
"""
from typing import List


class PriorityQueue:
    def __init__(self, keys=None, order=None):
        self.N = None
        self.keys = [None] + (keys if keys is not None else [])
        self.order = (lambda x, y: x if x <= y else y) if order is None else order
        self.heapify()

    def root(self):
        return 1

    def size(self):
        return len(self.keys) - 1 if self.N is None else self.N

    def last(self):
        return self.size()

    def key(self, i):
        return self.keys[i]

    def swap(self, i, j):
        self.keys[i], self.keys[j] = self.keys[j], self.keys[i]

    def up(self, i):
        return i // 2

    def left_index(self, i):
        return 2 * i

    def right_index(self, i):
        return 2 * i + 1

    def is_legit(self, node):
        return self.root() <= node <= self.last()

    def legit(self, node):
        return node if self.is_legit(node) else None

    def left(self, parent):
        return self.legit(self.left_index(parent))

    def right(self, parent):
        return self.legit(self.right_index(parent))

    def parent(self, child):
        return self.legit(self.up(child))

    def ordered(self, i, j):
        k, l = self.key(i), self.key(j)
        return i if self.order(k, l) == k else j

    def preferred(self, i, j):
        if not i and not j:
            return None
        if i and j:
            return self.ordered(i, j)
        return i if j is None else j

    def child(self, parent):
        return self.preferred(self.left(parent), self.right(parent))


    def balanced(self, parent, child):
        return self.preferred(parent, child) == parent

    def balanced_up(self, child):
        parent = self.parent(child)
        return parent is None or self.balanced(parent, child)

    def balanced_down(self, parent):
        child = self.child(parent)
        return child is None or self.balanced(parent, child)

    def unbalanced_parent(self, child):
        return self.parent(child) if not self.balanced_up(child) else None

    def unbalanced_child(self, parent):
        return self.child(parent) if not self.balanced_down(parent) else None

    def lift(self, child):
        parent = self.unbalanced_parent(child)
        if parent is not None:
            self.swap(child, parent)
        return parent

    def drop(self, parent):
        child = self.unbalanced_child(parent)
        if child is not None:
            self.swap(parent, child)
        return child

    def swim(self, child):
        while self.unbalanced_parent(child):
            child = self.lift(child)

    def sink(self, parent):
        while self.unbalanced_child(parent):
            parent = self.drop(parent)

    def heapify(self):
        for node in reversed(range(1, self.last())):
            self.sink(node)

    def push(self, key):
        self.keys.append(key)
        self.swim(self.last())

    def pop(self):
        self.swap(self.root(), self.last())
        top = self.keys.pop()
        self.sink(self.root())
        return top

    def sort(self):
        self.N = self.size()
        while self.N >= self.root():
            self.swap(self.root(), self.last())
            self.N -= 1
            self.sink(self.root())
        self.N = None
        return self.keys[1:]

    def sorted(self):
        result = self.sort()
        self.heapify()
        return result

    def print(self):
        print(self.keys[1:])

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) <= 1:
            return 0
        pq = PriorityQueue(keys=sticks)
        cost = 0
        while pq.size() > 1:
            first, second = pq.pop(), pq.pop()
            cost += first + second
            pq.push(first + second)
        return cost

if __name__ == '__main__':
    keys = [2, 3, 1, 5, 4, 7, 13, 27, 43, 12, 11]
    heap = PriorityQueue(keys=keys)
    print(heap.keys)
    heap.sort()
    heap.print()

