from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # problem type:
        # graph, since we'll be creating edges based on word patterns

        # approach:
        # should do bfs to find minimal number of steps
        # build adj list, pattern -> word list
        # take beginWord, get all possible patterns for it (replacing each char with *)
        # make a queue and add each pattern, checking our word map if the valid word
        # is contained in the value list. Queue up the patterns for each of these 
        # containing words and check. Track how many operations and return 
        # once we find it
        if endWord not in wordList:
            return 0
        adj = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adj[pattern].append(word)

        visit = set()
        queue = deque()
        queue.append(beginWord)
        steps = 1
        while queue:
            # go layer by layer
            for i in range(len(queue)):
                popped = queue.popleft()
                if popped == endWord:
                    return steps
                for i in range(len(popped)):
                    # build every pattern for the current word we just popped and queue all its neigbours
                    pattern = popped[:i] + "*" + popped[i + 1:]
                    for word in adj[pattern]:
                        if word in visit:
                            continue
                        queue.append(word)
                        visit.add(word)
            steps += 1
        return 0















