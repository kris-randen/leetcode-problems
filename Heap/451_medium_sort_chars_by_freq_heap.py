"""
451. Sort Characters By Frequency
Medium
company
Bloomberg
company
Amazon
company
Microsoft
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.



Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.


Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.
Accepted
510.6K
Submissions
727.8K
Acceptance Rate
70.1%

"""

class PriorityQueue:
    def __init__(self, keys=None, order=None):
        self.N = None
        self.keys = [None] + (keys if keys is not None else [])
        self.order = (lambda x, y: x if x <= y else y) if order is None else order
        self.heapify()

    def size(self):
        return len(self.keys) - 1 if self.N is None else self.N

    def is_empty(self):
        return self.size() == 0

    def root(self):
        return 1

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

    def left(self, parent):
        left = self.left_index(parent)
        return left if self.is_legit(left) else None

    def right(self, parent):
        right = self.right_index(parent)
        return right if self.is_legit(right) else None

    def is_leaf(self, node):
        return self.left(node) is None

    def is_root(self, node):
        return node == self.root()

    def ordered(self, i, j):
        k, l = self.key(i), self.key(j)
        return i if self.order(k, l) == k else j

    def preferred(self, i, j):
        if not i and not j:
            return None
        if i and j:
            return self.ordered(i, j)
        return i if not j else j

    def child(self, parent):
        return self.preferred(self.left(parent), self.right(parent))

    def parent(self, child):
        parent = self.up(child)
        return parent if self.is_legit(parent) else None

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
        if parent is None:
            return
        self.swap(child, parent)
        return parent

    def drop(self, parent):
        child = self.unbalanced_child(parent)
        if child is None:
            return
        self.swap(parent, child)
        return child

    def swim(self, child):
        while self.unbalanced_parent(child) is not None:
            child = self.lift(child)

    def sink(self, parent):
        while self.unbalanced_child(parent) is not None:
            parent = self.drop(parent)

    def heapify(self):
        for node in reversed(range(1, self.last())):
            self.sink(node)

    def pop(self):
        if self.is_empty():
            return None
        self.swap(self.root(), self.last())
        top = self.keys.pop()
        self.sink(self.root())
        return top

    def push(self, key):
        self.keys.append(key)
        self.swim(self.last())

    def sort(self):
        self.N = self.size()
        while self.N >= self.root():
            self.swap(self.root(), self.last())
            self.N -= 1
            self.sink(self.root())
        self.N = None

    def sorted(self):
        self.sort()
        result = self.keys[1:]
        self.heapify()
        return result

    def print(self):
        print(self.keys[1:])

class Solution:
    def frequencySort(self, s: str) -> str:
        order = lambda x, y: x if x[1] >= y[1] else y

        frequency = {}
        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

        pq = PriorityQueue(keys=list(frequency.items()), order=order)

        result = ""
        while not pq.is_empty():
            top = pq.pop()
            result += top[0] * top[1]
        return result


if __name__ == '__main__':
    keys = [2, 3, 1, 5, 4, 7, 13, 27, 43, 12, 11]
    heap = PriorityQueue(keys=keys)
    print(heap.keys)
    print(heap.sorted())
    heap.print()
    heap.sort()
    heap.print()


