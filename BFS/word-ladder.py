from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # all words are of same length as beginWord
        L = len(beginWord)

        mp = defaultdict(list)
        for word in wordList:
            for i in range(L):
                mp[word[:i] + '*' + word[i + 1:]].append(word)

        q = deque([])
        q.append((beginWord, 1))

        visited = set()
        visited.add(beginWord)

        while q:
            popped, level = q.popleft()

            # because we are doing bfs we will find the shortest path first
            for i in range(L):
                temp = popped[:i] + '*' + popped[i + 1:]
                for nei in mp[temp]:
                    if nei == endWord:
                        return level + 1

                    if nei not in visited:
                        q.append((nei, level + 1))
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
