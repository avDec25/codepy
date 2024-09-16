from typing import List
import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        adj = collections.defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                adj[pattern].append(word)

        q = collections.deque()
        q.append(beginWord)

        visited = set()
        visited.add(beginWord)

        ans = 1
        while q:
            for i in range(len(q)):
                popped = q.popleft()

                if popped == endWord:
                    return ans

                for j in range(len(popped)):
                    pattern = popped[:j] + "*" + popped[j + 1:]
                    for neighbour in adj[pattern]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            q.append(neighbour)
            ans += 1

        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))

beginWord = "hot"
endWord = "dog"
wordList = ["hot","dog"]
print(Solution().ladderLength(beginWord, endWord, wordList))
