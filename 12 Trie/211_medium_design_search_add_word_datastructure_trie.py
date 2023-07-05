"""

211. Design Add and Search Words Data Structure
Medium
7K
395
Companies
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

"""


class Trie:
    def __init__(self):
        self.nodes = {}
        self.ends = False

    def insert(self, word: str) -> None:
        curr = self
        for ch in word:
            if ch not in curr.nodes: curr.nodes[ch] = Trie()
            curr = curr.nodes[ch]
        curr.ends = True

    def search(self, word: str) -> bool:
        curr = self
        for ch in word:
            if ch not in curr.nodes: return False
            curr = curr.nodes[ch]
        return curr.ends

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for ch in prefix:
            if ch not in curr.nodes: return False
            curr = curr.nodes[ch]
        return True


def pattern(node, word: str, i: int) -> bool:
    if i >= len(word): return node.ends
    curr, found, ch = node, False, word[i]
    if ch == '.':
        for c in curr.nodes:
            found = found or pattern(curr.nodes[c], word, i + 1)
    elif ch != '.':
        if ch not in curr.nodes: return False
        found = found or pattern(curr.nodes[ch], word, i + 1)
    return found


class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return pattern(self.trie, word, 0)