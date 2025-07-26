"""
Trie (Prefix Tree)
- A type of tree structure consisting of characters typically for inserting and searching for words in constant time. 
  We could just use a hash map to insert and search for words in constant time, but a trie also lets us search *prefixes* in constant time.
  So if we had an entry in the trie, maybe "apple", we could simple search for the prefix "ap" and return if there's a match.

- Insert Word: O(1)
- Search Word: O(1)
- Search Prefix: O(1)

"""
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.word

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True





