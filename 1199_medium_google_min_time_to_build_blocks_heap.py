"""
1199. Minimum Time to Build Blocks
Hard
158
23
company
Google
You are given a list of blocks, where blocks[i] = t means that the i-th block needs t units of time to be built. A block can only be built by exactly one worker.

A worker can either split into two workers (number of workers increases by one) or build a block then go home. Both decisions cost some time.

The time cost of spliting one worker into two workers is given as an integer split. Note that if two workers split at the same time, they split in parallel so the cost would be split.

Output the minimum time needed to build all blocks.

Initially, there is only one worker.



Example 1:

Input: blocks = [1], split = 1
Output: 1
Explanation: We use 1 worker to build 1 block in 1 time unit.
Example 2:

Input: blocks = [1,2], split = 5
Output: 7
Explanation: We split the worker into 2 workers in 5 time units then assign each of them to a block so the cost is 5 + max(1, 2) = 7.
Example 3:

Input: blocks = [1,2,3], split = 1
Output: 4
Explanation: Split 1 worker into 2, then assign the first worker to the last block and split the second worker into 2.
Then, use the two unassigned workers to build the first two blocks.
The cost is 1 + max(3, 1 + max(1, 2)) = 4.


Constraints:

1 <= blocks.length <= 1000
1 <= blocks[i] <= 10^5
1 <= split <= 100
Accepted
3.8K
Submissions
9.3K
Acceptance Rate
41.0%
"""
from typing import List

# Too hard. I think it needs Huffman (that made sense). Peeked into one of the solutions. You have to go up from the bottom.


class PriorityQueue:
    def __init__(self, keys=None, order=None):
        self.items = [None] + ([] if keys is None else keys)
        self.order = lambda x, y: x if x <= y else y if order is None else order
        self.N = None
        self.heapify()

    def root(self):
        return 1

    def item(self, i):
        return self.items[i]

    def keys(self):
        return self.items[1:]

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def size(self):
        return len(self.items) - 1 if self.N is None else self.N

    def is_empty(self):
        return self.size() == 0

    def last(self):
        return self.size()

    def ordered(self, i, j):
        k, l = self.item(i), self.item(j)
        return i if self.order(k, l) == k else j

    def preferred(self, i, j):
        if not i and not j:
            return None
        if i and j:
            return self.ordered(i, j)
        return i if not j else j

    def up(self, i):
        return i // 2

    def down_left(self, i):
        return 2*i

    def down_right(self, i):
        return 2*i + 1

    def is_legit(self, node):
        return self.root() <= node <= self.last()

    def legit(self, node):
        return node if self.is_legit(node) else None

    def parent(self, child):
        return self.legit(self.up(child))

    def left(self, parent):
        return self.legit(self.down_left(parent))

    def right(self, parent):
        return self.legit(self.down_right(parent))

    def child(self, parent):
        return self.preferred(self.left(parent), self.right(parent))

    def balanced(self, parent, child):
        return self.preferred(parent, child) == parent

    def balanced_up(self, child, parent):
        return parent is None or self.balanced(parent, child)

    def balanced_down(self, parent, child):
        return child is None or self.balanced(parent, child)

    def unbalanced_parent(self, child):
        parent = self.parent(child)
        return parent if not self.balanced_up(child, parent) else None

    def unbalanced_child(self, parent):
        child = self.child(parent)
        return child if not self.balanced_down(parent, child) else None



    def drop(self, parent):
        child = self.unbalanced_child(parent)
        if child is not None:
            self.swap(parent, child)
        return child

    def lift(self, child):
        parent = self.unbalanced_parent(child)
        if parent is not None:
            self.swap(child, parent)
        return parent

    def sink(self, parent):
        while self.unbalanced_child(parent) is not None:
            parent = self.drop(parent)

    def swim(self, child):
        while self.unbalanced_parent(child) is not None:
            child = self.lift(child)





    def heapify(self):
        for node in reversed(range(self.root(), self.last())):
            self.sink(node)

    def push(self, key):
        self.items.append(key)
        self.swim(self.last())

    def pop(self) -> object:
        if self.is_empty():
            return None
        self.swap(self.root(), self.last())
        top = self.items.pop()
        self.sink(self.root())
        return top


    def sort(self):
        self.N = self.size()
        while self.N >= self.root():
            self.swap(self.root(), self.last())
            self.N -= 1
            self.sink(self.root())
        self.N = None


    def sorted(self):
        self.sort()
        keys = self.keys()
        self.heapify()
        return keys

    def print(self):
        print(self.keys())


def minBuildTime(blocks: List[int], split: int) -> int:
    if len(blocks) <= 1:
        return 0 if len(blocks) == 0 else blocks[0]

    min_pq = PriorityQueue(keys=blocks)
    max_pq = PriorityQueue(order=lambda x, y: x if x >= y else y)

    a, b = min_pq.pop(), min_pq.pop()
    max_pq.push(a), max_pq.push(b)

    while not min_pq.is_empty():
        max_pq.push(split + max_pq.pop())
        max_pq.push(min_pq.pop())

    return split + max_pq.pop()

if __name__ == '__main__':
    array = [2, 3, 1, 5, 4, 7, 13]
    pq = PriorityQueue(keys=array)
    pq.print()
    pq.sort()
    pq.print()
    pq.heapify()
    print(pq.sorted())
    pq.print()
    pq.push(9)
    pq.print()
    print(pq.sorted())