"""

208. Implement Trie (Prefix Tree)
Medium
10.4K
117
Companies
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.


Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

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


