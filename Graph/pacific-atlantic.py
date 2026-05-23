from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        def bfs(start):
            visited = set(start)
            q = deque(start)

            while q:
                r, c = q.popleft()
                for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and (nr, nc) not in visited
                            and heights[nr][nc] >= heights[r][c]
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))

            return visited

        pacific = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]
        both = bfs(pacific) & bfs(atlantic)
        return [[r, c] for r, c in both]


heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(Solution().pacificAtlantic(heights))

heights = [[1]]
print(Solution().pacificAtlantic(heights))
