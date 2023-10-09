"""
Data Structures
1. Union Find
2. Index Priority Queue
3. Left Leaning Red Black (LLRB) Binary Search Tree
4. Trie
5. LRU Cache
6. Interval Search Tree
7. kd-Tree
8.

Algorithms

a. Graphs
1. DFS
2. BFS
3. Dijkstra (SSSP non-negative) O(m log (n))
4. Bellman-Ford (SSSP) O(mn)
5. Floyd-Warshall (APSP) O(n ^ 3)
6. Johnson (APSP) O(mn * log (n))
7. Minimum Spanning Tree Prim
8. Minimum Spanning Tree Kruskal
9. Max Flow - Min Cut Ford Fulkerson
10. Strong Connected Components Kosaraju
11. DAG SSSP (general edge weights)

b. Trees
1.  1D Range Search
2. Line Segment Intersection
3. Rectangle Intersection
4. Huffman Encoding
5.

c. String
1. Knuth-Morris-Pratt
2. Boyer-Moore
3. Rabin-Karp



Patterns

Greedy
1. Fractional Knapsack
2. Scheduling

Dynamic Programming
1. Weight Independent Sets (WIS) in Path Graphs
2. Knapsack (Infinite)
3. Knapsack (Finite)
4. Sequence Alignment
"""

"""
==============
DATASTRUCTURES
==============
"""

"""
1. Union-Find
"""
"""
API
"""




"""
Implementation
"""



"""
2. Indexed Priority Queue
"""
"""
API
"""




"""
Implementation
"""





"""
3. LLRB
"""
"""
API

K: Key, V: Value, Z: Node

class Node

Optional[Node]      left
Optional[Node]      right
Value               val


class BST

Optional[Value]     get(key: Key)
Node                put(key: Key, val: Value)
Node                min()
Node                max()
Int                 size()
Int                 rank(key: Key)
(Key, Value)        select(index: Int)
Int                 range_count(lo: Key, hi: Key)
[Key]               range(lo: Key, hi: Key)
(Key, Value)        delete_min()
Optional[Node]      delete(key: Key)
Optional[Key]       ceil(key: Key)
Optional[Key]       floor(key: Key)

"""


"""
Implementation
"""

class Node:
    def __init__(self, key, val):
        self.key = key; self.val = val
        self.left = self.right = None
        self.count = 1; self.index = 0

    def get(self, key):
        if key == self.key: return self
        return self.left if key < self.key else self.right



class BST:
    def __init__(self, root):
        self.root = root

    def size(self, node):
        return 0 if not node else node.count

    def rank_at(self, node, key):
        if key == node.key:
            return self.size(node.left)
        if key < node.key:
            return self.rank_at(node.left, key)
        if key > node.key:
            return self.rank_at(node.right, key) + 1 + self.size(node.left)

    def rank(self, key):
        return self.rank_at(self.root, key)

    def get_at(self, node, key):
        if not node or key == node.key: return node
        if key < node.key: return self.get_at(node.left, key)
        if key > node.key: return self.get_at(node.right, key)

    def get(self, key): return self.get_at(self.root, key)

    def contains(self, key): return self.get(key)

    def put_at(self, node, key, val):
        if not node: return node
        if key < node.key: node.left = self.put_at(node.left, key, val)
        elif key > node.key: node.right = self.put_at(node.right, key, val)
        else: node.val = val
        node.count = 1 + self.size(node.left) + self.size(node.right)
        node.index = self.rank_at(node, node.key)
        return node

    def put(self, key, val):
        self.root = self.put_at(self.root, key, val)

    def unwrap_key(self, node):
        return None if not node else node.key

    def min_at(self, node):
        if not node or not node.left: return node
        return self.min_at(node.left)

    def min(self):
        return self.unwrap_key(self.min_at(self.root))

    def max_at(self, node):
        if not node or not node.right: return node
        return self.max_at(node.right)

    def max(self):
        return self.unwrap_key(self.max_at(self.root))

    def floor_at(self, node, key):
        if not node or key == node.key: return node
        if key < node.key: return self.floor_at(node.left, key)
        if key > node.key:
            t = self.floor_at(node.right, key)
            return t if t else node

    def floor(self, key):
        return self.unwrap_key(self.floor_at(self.root, key))

    def ceil_at(self, node, key):
        if not node or key == node.key: return node
        if key > node.key: return self.ceil_at(node.right, key)
        if key < node.key:
            t = self.ceil_at(node.right, key)
            return t if t else node

    def ceil(self, key):
        return self.unwrap_key(self.ceil_at(self.root, key))

    def delete_min_at(self, node):
        if not node: return node
        if not node.left: return node.right
        node.left = self.delete_min_at(node.left)
        node.count = 1 + self.size(node.left) + self.size(node.right)
        return node

    def delete_min(self):
        self.root = self.delete_min_at(self.root)

    def delete_at(self, node, key):
        if not node: return node
        if key < node.key:
            node.left = self.delete_at(node.left, key)
        elif key > node.key:
            node.right = self.delete_at(node.right, key)
        else:
            if not node.left: return node.right
            if not node.right: return node.left
            t = node
            node = self.min_at(node.right)
            node.right = self.delete_min_at(node.right)
            node.left = t.left
        node.count = 1 + self.size(node.left) + self.size(node.right)
        return node

    def delete(self, key):
        self.root = self.delete_at(self.root, key)





"""
4. Trie
"""
"""
API
"""




"""
Implementation
"""





"""
5. LRU Cache
"""
"""
API
"""




"""
Implementation
"""





"""
6. Interval Search Tree
"""
"""
API
"""




"""
Implementation
"""





"""
7. kd-Tree
"""
"""
API
"""




"""
Implementation
"""






"""
==========
ALGORITHMS
==========
"""
"""
a. Graphs
"""
"""
1. DFS
"""



"""
2. BFS
"""



"""
Single Source Shortest Paths (SSSP)
"""
"""
3. Dijkstra (non-negative)
"""



"""
4. Bellman-Ford (general)
"""



"""
5. DAG SSSP (general)
"""




"""
All Pairs Shortest Paths (APSP)
"""
"""
5. Floyd-Warshall
"""



"""
6. Johnson
"""




"""
5. Prim's MST
"""



"""
6. Kruskal's MST
"""



"""
7. Kosaraju's SCC
"""



"""
b. Trees
"""
"""
1. 1D Range Search
"""



"""
2. Line Segment Intersection
"""



"""
3. Rectangle Intersection
"""



"""
4. Huffman Encoding
"""




"""
c. String
"""
"""
Deterministic Finite Automaton DFA
"""

"""
1. Knuth-Morris-Pratt (KMP) 
"""


"""
2. Boyer-Moore
"""


"""
3. Rabin-Karp (Hashing)
"""



"""
==========
PATTERNS
==========
"""

"""
a. Recursion and Backtracking
"""



"""
b. Greedy
"""
"""
1. Scheduling
"""



"""
2. Knapsack (Fractional)
"""



"""
c. Dynamic Programming
"""
"""
1. Knapsack (with repetitions)
"""



"""
2. Knapsack (without repetitions)
"""



"""
3. Weight Independent Sets (WIS) in Path Graphs
"""



"""
4. Sequence Alignment
"""



"""
d. Two-Pointer
"""



"""
e. Sliding Window
"""
