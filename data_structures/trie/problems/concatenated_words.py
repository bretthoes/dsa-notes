"""
472. Concatenated Words
level: Hard
tags: Amazon
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words (not necessarily distinct) in the given array.
Example 1:
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Example 2:
Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
"""
from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        type: trie, dp (memoization)
        approach:
        add each word to a trie,
        check if each word exists in trie
        """
        result = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        for word in words:
            if trie.search(word):
                result.append(word)
        return result
    
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.word = True

    def search(self, word):
        def _search(index, count, memo):
            if index in memo:
                return memo[index]

            cur = self.root
            for i in range(index, len(word)):
                char = word[i]
                if char not in cur.children:
                    memo[index] = False
                    return False
                cur = cur.children[char]
                if cur.word:
                    if i == len(word) - 1:
                        memo[index] = count > 1
                        return count >= 1
                    if _search(i + 1, count + 1, memo):
                        memo[index] = True
                        return True
            memo[index] = False
            return False

        return _search(0, 0, {})







