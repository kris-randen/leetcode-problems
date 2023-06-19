"""
1061. Lexicographically Smallest Equivalent String Medium

You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.



Example 1:

Input: s1 = "parker", s2 = "morris", baseStr = "parser"
Output: "makkek"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
The characters in each group are equivalent and sorted in lexicographical order.
So the answer is "makkek".
Example 2:

Input: s1 = "hello", s2 = "world", baseStr = "hold"
Output: "hdld"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".
Example 3:

Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
Output: "aauaaaaada"
Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".


Constraints:

1 <= s1.length, s2.length, baseStr <= 1000
s1.length == s2.length
s1, s2, and baseStr consist of lowercase English letters.
Accepted
69.6K
Submissions
90.9K
Acceptance Rate
76.5%

"""
import string
from heapq import *

class UnionFind:
    def __init__(self, n=0, nodes=None, count=None):
        self.__nodes = nodes
        self.__node_map = {node: index for index, node in enumerate(self.__nodes)}
        self.__n = n if self.__nodes is None else len(nodes)
        self.__ind = range(self.__n)
        self.__id = [node for node in self.__ind]
        self.__count = self.__n if count is None else count
        self.__components = {root: [root] for root in self.__ind}

    def __parent(self, node):
        return self.__id[node]

    def __assign(self, node, parent):
        self.__id[node] = parent

    def __path(self, node):
        path = [node]
        while node != self.__parent(node):
            node = self.__parent(node)
            path.append(node)
        return path

    def __compress(self, path):
        root = path[-1]
        for node in path:
            self.__assign(node=node, parent=root)

    def __size(self, root):
        return len(self.__components[root])

    def __separate(self, a, b):
        p, q = self.root(a), self.root(b)
        small = p if self.__size(p) < self.__size(q) else q
        large = q if self.__size(q) > self.__size(p) else p
        return small, large

    def __merge(self, large, small):
        for node in self.__components.pop(small):
            heappush(self.__components[large], node)

    def root(self, node):
        path = self.__path(node)
        self.__compress(path)
        return path[-1]

    def find_index(self, node):
        index = self.__node_map[node]
        return self.__components[self.root(index)][0]

    def find(self, node):
        index = self.find_index(node)
        return index if self.__nodes is None else self.__nodes[index]

    def count(self):
        return self.__count

    def connected(self, a, b):
        return self.root(a) == self.root(b)

    def union_index(self, a, b):
        if self.connected(a, b):
            return
        s, l = self.__separate(a, b)
        self.__assign(node=s, parent=l)
        self.__merge(l, s)
        self.__count -= 1

    def union(self, a, b):
        self.union_index(self.__node_map[a], self.__node_map[b])

    def print(self):
        print(f"node map = {self.__node_map}")
        print(f"components = {self.__components}")

def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
    components = UnionFind(nodes=list(string.ascii_lowercase))
    components.print()
    for ind, char in enumerate(s1):
        print(type(ind), ind, char, s1[ind])
        components.union(s1[ind], s2[ind])

    return "".join(map(lambda x: components.find(x), baseStr))

if __name__ == '__main__':
    print(smallestEquivalentString('parker', 'morris', 'parser'))