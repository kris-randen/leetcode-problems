"""
127. Word Ladder
Hard
10.5K
1.8K
company
Uber
company
Apple
company
Amazon
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

"""

from collections import defaultdict

def gen_perms(word):
    words = [word]
    for i in range(len(word)):
        words.append(word[:i] + '*' + word[i + 1:])
    return words

class Graph:
    def __init__(self, words):
        self.words = words
        self.vertices = defaultdict(list)
        for word in words:
            perms = gen_perms(word)
            for i in range(1, len(perms)):
                self.vertices[word].append(perms[i])
                self.vertices[perms[i]].append(word)

class BFS:
    def __init__(self, G: Graph):
        self.G = G

    def execute(self, s, v):
        l, visited = 0, set()
        if s not in self.G.vertices or v not in self.G.vertices:
            return l
        q = [s]
        for p in q:
            visited.add(p)
            cs = self.G.vertices[p]
            for c in cs:
                if c == v: return l // 2
                q.append(c)
            l += 1
        return 0

def word_ladder(beginWord, endWord, wordList):
    perms, g = gen_perms(beginWord), Graph(wordList);
    min_length, bfs = 0, BFS(g)
    for perm in perms:
        min_length = min(min_length, bfs.execute(perm, endWord))
    return min_length

