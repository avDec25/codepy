from collections import defaultdict, deque
from typing import Optional, List


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
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(x, y):
            grid[x][y] = 0

            for nx, ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                    dfs(nx, ny)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)

        return islands

    def hasPathSumDFS(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stk = []
        stk.append((root, 0))
        while stk:
            top, sm = stk.pop()
            if top.left:
                stk.append((top.left, sm + top.val))
            if top.right:
                stk.append((top.right, sm + top.val))
            if top.left is None and top.right is None:
                if top.val + sm == targetSum:
                    return True
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, sm):
            if not node:
                return False
            if node.left is None and node.right is None:
                return sm + node.val == targetSum
            return dfs(node.left, node.val + sm) or dfs(node.right, node.val + sm)

        return dfs(root, 0)

    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
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

    def canFinishDFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0 for _ in range(numCourses)]
        # 0 unvisited
        # 1  visiting
        # 2   visited

        def hasCycle(node):
            if state[node] == 2:
                return False

            if state[node] == 1:
                return True

            state[node] = 1
            for nei in graph[node]:
                if hasCycle(nei):
                    return True
            state[node] = 2

            return False

        for i in range(numCourses):
            if hasCycle(i):
                return False

        return True


    def canFinishBFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        q = deque()
        for i, degree in enumerate(in_degree):
            if degree == 0:
                q.append(i)

        taken = 0
        while q:
            taken += 1
            popped = q.popleft()
            for nei in graph[popped]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return taken == numCourses


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(Solution().numIslands(grid))

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(Solution().numIslands(grid))
