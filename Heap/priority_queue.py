from copy import deepcopy

class IndexPQ:
    def __init__(self, keys=None, order=None):
        self.order = (lambda x, y: x if x <= y else y) if not order else order
        self.keys = [None] + (list(keys) if keys else [])
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

    def pop(self) -> object:
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



class PriorityQueue:
    def __init__(self, keys=None, order=None):
        self.N = None
        self.order = (lambda x, y: x if x <= y else y) if not order else order
        self.keys = [None] + keys if keys else [None]
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