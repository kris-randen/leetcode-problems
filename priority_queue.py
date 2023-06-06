from copy import deepcopy

class PriorityQueue:
    def __init__(self, order=None, keys=None):
        self.N = None
        self.order = lambda x, y: x if x <= y else y if not order else order
        self.keys = [None]
        if keys:
            self.keys[1:] = keys
        self.heapify()

    def root(self):
        return 1

    def last(self):
        return self.size()

    def key(self, i):
        return self.keys[i]

    def pref(self, i, j):
        if not i and not j:
            return None
        if i and j:
            k, l = self.keys[i], self.keys[j]
            return i if self.order(k, l) == k else j
        return i if not j else j

    def size(self):
        return len(self.keys) - 1 if self.N is None else self.N

    def is_empty(self):
        return self.size() == 0

    def is_root(self, i):
        return i == 1

    def up(self, i):
        return i // 2

    def parent(self, child):
        return self.up(child) if not self.is_root(child) else None

    def left(self, i):
        return 2*i

    def right(self, i):
        return 2*i + 1

    def is_legit(self, child):
        return child <= self.size()

    def left_child(self, parent):
        child = self.left(parent)
        return child if self.is_legit(child) else None

    def right_child(self, parent):
        child = self.right(parent)
        return child if self.is_legit(child) else None

    def no_left_child(self, parent):
        return not self.left_child(parent)

    def is_leaf(self, i):
        return self.no_left_child(i)

    def pref_child(self, parent):
        if self.is_leaf(parent):
            return None
        return self.pref(self.left_child(parent), self.right_child(parent))

    def swap(self, i, j):
        self.keys[i], self.keys[j] = self.keys[j], self.keys[i]

    def balanced(self, parent, child):
        return self.pref(parent, child) == parent

    def balanced_up(self, child):
        return self.is_root(child) or self.balanced(self.parent(child), child)

    def balanced_down(self, parent):
        child = self.pref_child(parent)
        return child is None or self.balanced(parent, child)

    def unbalanced_up(self, child):
        return None if self.balanced_up(child) else self.parent(child)

    def unbalanced_down(self, parent):
        result = None if self.balanced_down(parent) else self.pref(parent, self.pref_child(parent))
        return result

    def lift(self, child):
        parent = self.unbalanced_up(child)
        if not parent:
            return
        self.swap(child, parent)
        return parent

    def drop(self, parent):
        child = self.unbalanced_down(parent)
        if not child:
            return
        self.swap(parent, child)
        return child

    def swim(self, child):
        while self.unbalanced_up(child):
            child = self.lift(child)

    def sink(self, parent):
        while self.unbalanced_down(parent):
            parent = self.drop(parent)

    def heapify(self):
        for node in reversed(range(1, len(self.keys))):
            self.sink(node)

    def push(self, key):
        self.keys.append(key)
        self.swim(self.size())

    def pop(self):
        self.swap(1, self.size())
        key = self.keys.pop()
        self.sink(1)
        return key

    def find_rec(self, key, node):
        if self.is_empty() or not node:
            return None
        if self.keys[node] == key:
            return node
        if self.order(key, self.key(node)) == key:
            return None
        if self.order(key, self.key(node)) == self.key(node):
            left = self.find_rec(key, self.left_child(node))
            right = self.find_rec(key, self.right_child(node))
            return left if left else right

    def find(self, key):
        return self.find_rec(key, self.root())

    def delete(self, key: object) -> object:
        found = self.find(key)
        if not found:
            return None
        self.swap(found, self.last())
        self.N = self.size()
        self.N -= 1
        self.sink(found)
        return self.keys.pop()

    def sort(self):
        self.N = self.size()
        while self.N >= 1:
            self.swap(1, self.N)
            self.N -= 1
            self.sink(1)
        self.N = None

    def sorted(self):
        self.sort()
        result = self.keys[1:]
        self.heapify()
        return result

    def print(self):
        print(self.keys)

    def peek(self):
        return None if self.is_empty() else deepcopy(self.keys[1])


if __name__ == '__main__':
    keys = [2, 3, 1, 5, 4, 7, 13, 27, 43, 12, 11]
    heap = PriorityQueue(keys=keys)
    print(heap.keys)
    print(heap.sorted())
    heap.print()
    heap.push(57)
    heap.print()
    heap.pop()
    heap.print()
    print(heap.peek())
    # noinspection PyNoneFunctionAssignment
    deleted = heap.delete(5)
    print(f"deleted = {deleted}")
    deleted = heap.delete(27)
    print(f"deleted = {deleted}")
    deleted = heap.delete(57)
    print(f"deleted = {deleted}")
    deleted = heap.delete(43)
    print(f"deleted = {deleted}")
    deleted = heap.delete(27)
    print(f"deleted = {deleted}")
    heap.push(27)
    heap.push(27)
    heap.print()