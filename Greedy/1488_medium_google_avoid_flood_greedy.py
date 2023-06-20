"""
1488. Avoid Flood in The City
Medium
1.4K
263
company
Amazon
company
MindTickle
Oracle
Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake that is full of water, there will be a flood. Your goal is to avoid floods in any lake.

Given an integer array rains where:

rains[i] > 0 means there will be rains over the rains[i] lake.
rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
Return an array ans where:

ans.length == rains.length
ans[i] == -1 if rains[i] > 0.
ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.



Example 1:

Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.
Example 2:

Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.
Example 3:

Input: rains = [1,2,0,1,2]
Output: []
Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.

"""

import heapq

from collections import defaultdict

class IndexPQ:
    def __init__(self, keys=None, order=None):
        self.order = (lambda x, y: x if x <= y else y) if not order else order
        self.keys = [None] + (keys if keys else [])
        self.l = len(self.keys)
        self.id = dict() if not keys else {key: i for i, key in enumerate(self.keys)}
        self.pq = [-1] + ([_ for _ in range(1, self.l)] if keys else [])
        self.qp = [-1] + ([_ for _ in range(1, self.l)] if keys else [])
        self.N = None
        self.heapify()


    def ordered(self, i, j):
        assert(self.legit(i) and self.legit(j))
        return i if self.order(self.key(i), self.key(j)) == self.key(i) else j

    def preferred(self, i, j):
        if not i and not j: return None
        if not i: return j
        if not j: return i
        return self.ordered(i, j)

    @property
    def n(self):
        return self.size

    @property
    def top(self):
        return 1 if not self.empty() else None

    @property
    def last(self):
        return self.n

    @property
    def size(self):
        return len(self.keys) - 1 if self.N is None else self.N

    def empty(self):
        return self.size == 0

    def is_legit(self, i):
        return 0 < i <= self.size

    def legit(self, i):
        return i if self.is_legit(i) else None

    def key(self, i):
        return self.keys[self.pq[i]] if self.is_legit(i) else None

    def root(self, i):
        return i == 1

    def leaf(self, i):
        return self.child(i) is None

    def up(self, i):
        return i // 2

    def lt(self, i):
        return 2*i

    def rt(self, i):
        return 2*i + 1

    def parent(self, c):
        return self.legit(self.up(c))

    def left(self, p):
        return self.legit(self.lt(p))

    def right(self, parent):
        return self.legit(self.rt(parent))

    def child(self, p):
        return self.preferred(self.left(p), self.right(p))

    def balanced_up(self, c):
        p = self.parent(c)
        if not p: return True
        return self.preferred(c, p) == p

    def balanced_down(self, p):
        c = self.child(p); return self.preferred(p, c) == p

    def unbal_parent(self, c):
        return None if self.balanced_up(c) else self.parent(c)

    def unbal_child(self, p):
        return None if self.balanced_down(p) else self.child(p)

    def swap(self, i, j):
        assert (self.legit(i) and self.legit(j))
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]] = i; self.qp[self.pq[j]] = j

    def lift(self, c):
        p = self.unbal_parent(c)
        if not p: return None
        self.swap(p, c); return p

    def drop(self, p):
        c = self.unbal_child(p)
        if not c: return None
        self.swap(p, c); return c

    def swim(self, c):
        while not self.balanced_up(c): c = self.lift(c)

    def sink(self, p):
        while not self.balanced_down(p): p = self.drop(p)

    def heapify(self):
        for p in reversed(range(1, len(self.keys))):
            self.sink(p)

    def push(self, key):
        self.keys.append(key)
        self.swim(self.n)

    def pop(self):
        t = self.pq[self.top]; pref = self.keys[t]
        self.swap(self.top, self.last)
        self.pq.pop()
        del self.qp[t]; del self.keys[t]
        return pref

    def change(self, i, key):
        self.keys[i] = key
        self.swim(self.qp[i])
        self.sink(self.qp[i])

    def sort(self):
        self.N = self.size
        while self.N > self.top:
            self.print()
            self.swap(self.top, self.last)
            self.N -= 1
            self.sink(self.top)
        self.N = None

    def print(self):
        print(f'keys = {self.keys}')
        print(f'pq = {self.pq}')
        print(f'qp = {self.qp}')



class Lake:
    def __init__(self, lake=0, rain=0):
        self.lake = lake
        self.rain = rain

    def __lt__(self, other):
        return self.rain < other.rain

def avoid_flood(rains):
    rained, excess, ans = defaultdict(int), 0, []
    for rain in rains:
        if rain and rain in rained:
            excess += 1
        rained[rain] += 1
        if excess > rained[0]: return []
    lakes = list(map(lambda x: Lake(x[0], x[1]), rained.items()))
    lakes.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for rain in rains:
        if rain:
            ans.append(-1)
        if not rain:
            if i >= len(lakes):
                ans.append(1)
            else:
                ans.append(lakes[i])
    return ans



if __name__ == '__main__':
    v = [(1, 5), (2, 3), (3, 4), (4, 17), (5, 13), (6, 11), (7, 19)]
    pq = IndexPQ(keys=v, order=(lambda x, y: x if x[1] >= y[1] else y))
    pq.change(3, (3, 23))
    print(f'changed')
    pq.print()
    pq.sort()
    pq.print()