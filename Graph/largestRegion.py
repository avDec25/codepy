from collections import deque


def largest_region(grid, m, n):
    largest_region_size = float('-inf')
    visited = set()
    q = deque()
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1 and (r, c) not in visited:
                q.append((r, c))
                visited.add((r, c))
                region_size = 1
                while q:
                    pr, pc = q.popleft()
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1),
                                   (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                        nr = pr + dx
                        nc = pc + dy
                        if (0 <= nr < m) and (0 <= nc < n) and grid[nr][
                            nc] == 1 and (nr, nc) not in visited:
                            region_size += 1
                            visited.add((nr, nc))
                            q.append((nr, nc))

                largest_region_size = max(region_size, largest_region_size)
    return largest_region_size


grid = [[1, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0],
        [1, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0, 1, 1]]

grid = [[0, 0, 1, 1, 0],
         [1, 0, 1, 1, 0],
         [0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1]]
m = len(grid)
n = len(grid[0])
print(largest_region(grid, m, n))
