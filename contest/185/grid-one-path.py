class Solution:
    def createGrid(self, rows: int, cols: int) -> list[str]:
        grid = [['.' for _ in range(cols)] for _ in range(rows)]
        if rows == 1 or cols == 1:
            return ["".join(grid[r]) for r in range(rows)]

        grid[0][cols-1] = '#'
        for c in range(cols-2):
            grid[1][c] = '#'
        if rows > 2:
            for r in range(2, rows):
                for c in range(cols-1):
                    grid[r][c] = '#'
        return ["".join(grid[r]) for r in range(rows)]