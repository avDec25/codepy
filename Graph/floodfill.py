from collections import deque


def neighbors(grid, x, y):
    R = len(grid)
    C = len(grid[0])
    ans = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 1:
            ans.append((nx, ny))
    return ans


def floodFill(grid, x, y, newClr):
    visited = set()
    q = deque()
    q.append((x, y))
    visited.add((x, y))
    grid[x][y] = newClr
    while q:
        px, py = q.popleft()
        for nx, ny in neighbors(grid, px, py):
            if (nx, ny) not in visited:
                grid[nx][ny] = newClr
                visited.add((nx, ny))
                q.append((nx, ny))

    for r in range(len(grid)):
        print(grid[r])


grid = [[1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]]
x = 1
y = 1
newClr = 3
floodFill(grid, x, y, newClr)
