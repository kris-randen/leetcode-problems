"""

215. Kth Largest Element in an Array
Medium
14.4K
708
Companies
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

"""

# Index Heap Practice

class IndexHeap:
    def __init__(self, n, order=None):
        self.keys = [None] * (n + 1)
        self.pq = [-1 for _ in range(n + 1)]
        self.qp = [-1 for _ in range(n + 1)]
        self.order = order if order else (lambda x, y: x if x > y else y)
        self.n = 0

    def key(self, i):
        return self.keys[self.pq[i]]

    def ord(self, i, j):
        p, q = self.key(i), self.key(j); o = self.order(p, q)
        return i if p == o else j

    def pref(self, i, j):
        if not i and not j: return None
        if not i: return j
        if not j: return i
        return self.ord(i, j)

    def up(self, i): return i // 2

    def lt(self, i): return 2 * i

    def rt(self, i): return 2 * i + 1

    def is_legit(self, i): return 1 <= i <= self.n

    def legit(self, i): return i if self.is_legit(i) else None

    def parent(self, c): return self.legit(self.up(c))

    def left(self, p): return self.legit(self.lt(p))

    def right(self, p): return self.legit(self.rt(p))

    def child(self, p): return self.pref(self.left(p), self.right(p))

    def bal_up(self, c):
        p = self.parent(c)
        if not p: return True
        return self.pref(c, p) == p

    def bal_down(self, p):
        c = self.child(p)
        return self.pref(c, p) == p

    def unbal_parent(self, c):
        return self.parent(c) if not self.bal_up(c) else None

    def unbal_child(self, p):
        return self.child(p) if not self.bal_down(p) else None

    def swap(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]] = i; self.qp[self.pq[j]] = j

    def lift(self, c):
        p = self.unbal_parent(c)
        if p: self.swap(p, c); return p

    def drop(self, p):
        c = self.unbal_child(p)
        if c: self.swap(p, c); return c

    def swim(self, c):
        while not self.bal_up(c): c = self.lift(c)

    def sink(self, p):
        while not self.bal_down(p): p = self.drop(p)

    def push(self, i, key):
        self.n += 1
        self.pq[self.n] = i
        self.qp[i] = self.n
        self.swim(self.n)
        pass

