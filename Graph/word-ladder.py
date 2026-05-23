from typing import List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        L = len(beginWord)
        adj_cells = defaultdict(list)
        for word in wordList:
            for i in range(L):
                generic_word = word[:i] + '*' + word[i + 1:]
                adj_cells[generic_word].append(word)

        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            word, level = q.popleft()
            for i in range(L):
                generic_word = word[:i] + '*' + word[i+1:]
                for nei in adj_cells[generic_word]:
                    if nei == endWord:
                        return level + 1
                    if nei not in visited:
                        q.append((nei, level+1))
                        visited.add(nei)

        return 0




beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]
print(Solution().ladderLength(beginWord, endWord, wordList))
