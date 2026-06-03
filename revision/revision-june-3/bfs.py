from collections import deque, defaultdict
from pydoc import visiblename
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        visited = set()
        visited.add(root)
        ans = []
        while q:
            n = len(q)
            intermediate = []
            while n:
                node = q.popleft()
                intermediate.append(node.val)
                if node.left and node.left not in visited:
                    q.append(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)
                n -= 1
            ans.append(intermediate)
        return ans

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque([])
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        time = 0
        while q and fresh > 0:
            time += 1
            n = len(q)
            while n:
                x, y = q.popleft()
                for nx, ny in [(x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)]:
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))
                n -= 1

        return time if fresh == 0 else -1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        mp = defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                mp[word[:i] + '*' + word[i + 1:]].append(word)

        q = deque([])
        q.append((beginWord, 1))

        visited = set()
        visited.add(beginWord)

        while q:
            word, level = q.popleft()
            for i in range(L):
                generic_word = word[:i] + '*' + word[i + 1:]

                for nei in mp[generic_word]:
                    if nei == endWord:
                        return level + 1
                    if nei not in visited:
                        q.append((nei, level + 1))
                        visited.add(nei)
        return 0


grid = [[2, 1, 1], [1, 1, 1], [1, 1, 1]]
print(Solution().orangesRotting(grid))

grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(Solution().orangesRotting(grid))

grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
print(Solution().orangesRotting(grid))
