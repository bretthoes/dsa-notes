from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]):
        # type;
        # hash map
        # approach:
        # define a hash map to map a tuple of counts of letters to a list of words
        # iterate thru words, get count of each using an array of 26 0s,
        # convert this to a tuple and use this as a key
        # return a list of all values in this map
        result = defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord('a')] += 1
            result[tuple(counts)].append(word)
        return list(result.values())
