"""

212. Word Search II
Hard
8.6K
404
Companies
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

"""

from collections import defaultdict

class Trie:
    def __init__(self, words=None):
        self.chars = defaultdict(Trie)
        self.ends = False
        self.words = set(words) if words else set()
        for word in self.words: self.add(word)

    def contains(self, char):
        return char in self.chars

    def add(self, word):
        cur = self
        for char in word: cur = cur.chars[char]
        cur.ends = True; self.words.add(word)

    def search(self, word):
        cur = self
        for char in word:
            if not cur.contains(char): return None
            cur = cur.chars[char]
        return cur if cur.ends else None

    def starts(self, pref):
        cur = self
        for char in pref:
            if not cur.contains(char): return None
            cur = cur.chars[char]
        return cur


def right(j):
    return 0 <= j

def left(n, j):
    return j < n

def bottom(i):
    return 0 <= i

def top(m, i):
    return i < m

def valid(m, n, i, j):
    return right(j) and left(n, j) and bottom(i) and top(m, i)


def neighbors_ind(m, n, i, j):
    return filter(lambda p: valid(m, n, p[0], p[1]),
                  [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                  )

def neighbors(b, p):
    return neighbors_ind(len(b), len(b[0]), p[0], p[1])

def char(b, p):
    return b[p[0]][p[1]]

def traverse(b, trie):
    m, n, words = len(b), len(b[0]), set()

    def dfs(p, node, pref, visited):
        nonlocal words
        if p in visited:
            return
        c = char(b, p)
        if not node.contains(c):
            visited.clear()
            return
        pref += c
        visited.add(p)
        node = node.chars[c]
        nbs = neighbors(b, p)
        if node.ends:
            words.add(pref)
        for nb in nbs:
            dfs(nb, node, pref, visited)
        # visited.clear()
        return

    for i in range(m):
        for j in range(n):
            print(f'calling dfs for i = {i}, j = {j}')
            dfs((i, j), trie, '', set())
    return words


if __name__ == '__main__':
    trie = Trie(["oath","pea","eat","rain"])
    # trie = Trie(["aaaaa"])
    # b = [["a", "a"], ["a", "a"]]
    b = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    print(traverse(b, trie))


