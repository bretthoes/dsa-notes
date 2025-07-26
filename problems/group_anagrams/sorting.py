from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        for word in strs:
            # check if an anagram list exists already in res
            found = False
            for anagrams in res:
                if len(anagrams) > 0 and self.areAnagrams(word, anagrams[0]):
                    anagrams.append(word)
                    found = True
                    break
            if not found:
                res.append([word])

        return res

    def areAnagrams(self, source: str, target: str):
        return sorted(source) == sorted(target)
