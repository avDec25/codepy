from collections import deque, defaultdict
from typing import List, Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []
        while q:
            n = len(q)
            temp = []
            while n:
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                n -= 1
            ans.append(temp)
        return ans

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        time_taken = 0
        while q and fresh > 0:
            n = len(q)
            time_taken += 1
            while n:
                x, y = q.popleft()
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        q.append((nx, ny))
                        grid[nx][ny] = 2
                        fresh -= 1
                n -= 1

        return time_taken if fresh == 0 else -1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                generic_word = word[:i] + '*' + word[i + 1:]
                adj[generic_word].append(word)

        q = deque()
        q.append((beginWord, 0))
        seen = set()
        seen.add(beginWord)
        # bfs will guarantee Shortest path
        while q:
            n = len(q)
            while n:
                word, level = q.popleft()
                if word == endWord:
                    return level + 1
                else:
                    for i in range(L):
                        generic_word = word[:i] + '*' + word[i + 1:]
                        for neighbor in adj[generic_word]:
                            if neighbor not in seen:
                                q.append((neighbor, level + 1))
                                seen.add(neighbor)
                n -= 1
        return 0

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def explore_island(i, j):
            grid[i][j] = "0"
            stk = []
            stk.append((i, j))
            while stk:
                r, c = stk.pop()
                for nx, ny in [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        stk.append((nx, ny))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1
                    explore_island(i, j)

        return islands

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def path_sum(node, sum_so_far):
            if not node:
                return False

            if node.left is None and node.right is None:
                if node.val + sum_so_far == targetSum:
                    return True

            left_sum = path_sum(node.left, sum_so_far + node.val)
            right_sum = path_sum(node.right, sum_so_far + node.val)

            return left_sum or right_sum

        return path_sum(root, 0)

    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        if not root:
            return None
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(root)

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)

        state = [0 for _ in range(numCourses)]

        def has_cycle(node):
            if state[node] == 2:
                return False

            if state[node] == 1:
                return True

            state[node] = 1
            for nei in adj[node]:
                if has_cycle(nei):
                    return True
            state[node] = 2
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return False

        return True
