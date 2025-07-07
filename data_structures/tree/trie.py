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
        pass

    def search(self, word):
        pass

    def startsWith(self, prefix):
        pass

