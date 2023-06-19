"""
2336. Smallest Number in Infinite Set
Medium

Company
Amazon
Google

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.


Example 1:

Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.


Constraints:

1 <= num <= 1000
At most 1000 calls will be made in total to popSmallest and addBack.
Accepted
87.3K
Submissions
116.6K
Acceptance Rate
74.9%
"""

from copy import deepcopy

class PriorityQueue:
    def __init__(self, keys=None, order=None):
        self.keys = [None]
        if keys:
            self.keys[1:] = keys
        self.order = order if order else lambda x, y: x if x <= y else y
        self.N = None
        self.heapify()

    def ordered(self, i, j):
        k, l = self.key(i), self.key(j)
        return i if self.order(k, l) == k else j

    def pref(self, i, j):
        if not i and not j:
            return None
        if i and j:
            return self.ordered(i, j)
        return i if not j else j

    def size(self):
        return len(self.keys) - 1 if self.N is None else self.N

    def is_empty(self):
        return self.size() == 0

    def root(self):
        return 1

    def last(self):
        return self.size()

    def is_root(self, node):
        return node == self.root()

    def key(self, i):
        return self.keys[i]

    def up(self, i):
        return i // 2

    def left(self, i):
        return 2*i

    def right(self, i):
        return 2*i + 1

    def swap(self, i, j):
        self.keys[i], self.keys[j] = self.keys[j], self.keys[i]

    def is_legit(self, child):
        return self.root() <= child <= self.last()

    def is_leaf(self, node):
        return not self.is_legit(self.left(node))

    def left_child(self, parent):
        child = self.left(parent)
        return child if self.is_legit(child) else None

    def right_child(self, parent):
        child = self.right(parent)
        return child if self.is_legit(child) else None

    def child(self, parent):
        return self.pref(self.left_child(parent), self.right_child(parent))

    def parent(self, child):
        parent = self.up(child)
        return parent if self.is_legit(parent) else None

    def balanced(self, parent, child):
        return self.pref(parent, child) == parent

    def balanced_up(self, child):
        parent = self.parent(child)
        if not parent or self.pref(child, parent) == parent:
            return True
        return False

    def balanced_down(self, parent):
        child = self.child(parent)
        return child is None or self.balanced(parent, child)

    def unbalanced_parent(self, child):
        return self.parent(child) if not self.balanced_up(child) else None

    def unbalanced_child(self, parent):
        return self.child(parent) if not self.balanced_down(parent) else None

    def lift(self, child):
        parent = self.unbalanced_parent(child)
        if parent:
            self.swap(child, parent)
        return parent

    def drop(self, parent):
        child = self.unbalanced_child(parent)
        if child:
            self.swap(parent, child)
        return child

    def swim(self, child):
        while self.unbalanced_parent(child):
            child = self.lift(child)

    def sink(self, parent):
        while self.unbalanced_child(parent):
            parent = self.drop(parent)

    def push(self, key):
        self.keys.append(key)
        self.swim(self.last())

    def pop(self) -> object:
        self.swap(self.root(), self.last())
        popped = self.keys.pop()
        self.sink(self.root())
        return popped

    def peek(self):
        return deepcopy(self.key(self.root()))

    def heapify(self):
        for node in reversed(range(1, self.size())):
            self.sink(node)

    def sort(self):
        self.N = self.size()
        while self.N >= self.root():
            self.swap(self.root(), self.last())
            self.N -= 1
            self.sink(self.root())
        self.N = None

    def print(self):
        print(self.keys)


class SmallestInfiniteSet:
    def __init__(self):
        self.count = 1
        self.added = PriorityQueue()
        self.added_set = set()

    def popSmallest(self) -> int:
        if not self.added.is_empty():
            num = self.added.pop()
            self.added_set.remove(num)
            return num
        smallest = self.count
        self.count += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num >= self.count or num in self.added_set:
            return None
        self.added.push(num)

if __name__ == '__main__':
    keys = [2, 3, 1, 5, 4, 7, 13, 27, 43, 12, 11]
    heap = PriorityQueue(keys=keys)
    heap.print()
    heap.sort()
