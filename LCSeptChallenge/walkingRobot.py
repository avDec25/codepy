from collections import defaultdict
from typing import List


class Solution:
    def updateDir(self, dir, cmd):
        if dir == (0, 1):
            if cmd == -2: dir = (-1, 0)
            if cmd == -1: dir = (1, 0)
        elif dir == (-1, 0):
            if cmd == -2: dir = (0, -1)
            if cmd == -1: dir = (0, 1)
        elif dir == (0, -1):
            if cmd == -2: dir = (1, 0)
            if cmd == -1: dir = (-1, 0)
        elif dir == (1, 0):
            if cmd == -2: dir = (0, 1)
            if cmd == -1: dir = (0, -1)
        return dir

    def search(self, x, y, nx, ny, x_obstacles, y_obstacles, dir):
        if dir == (0, 1):
            obstacles = x_obstacles[x]
            for [p, q] in obstacles:
                if p == x and y < q <= ny:
                    return [p, q - 1]

        elif dir == (1, 0):
            obstacles = y_obstacles[y]
            for [p, q] in obstacles:
                if q == y and x < p <= nx:
                    return [p - 1, q]

        elif dir == (-1, 0):
            obstacles = y_obstacles[y]
            for [p, q] in obstacles:
                if q == y and nx <= p < x:
                    return [p + 1, q]

        elif dir == (0, -1):
            obstacles = x_obstacles[x]
            for [p, q] in obstacles:
                if p == x and ny <= q < y:
                    return [p, q + 1]

        return [nx, ny]

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = 0
        y = 0
        dir = (0, 1)
        ans = 0
        x_obstacles = defaultdict(list)
        y_obstacles = defaultdict(list)
        for [p, q] in obstacles:
            x_obstacles[p].append([p, q])
            y_obstacles[q].append([p, q])

        for cmd in commands:
            if cmd > 0:
                cand_x = x + dir[0] * cmd
                cand_y = y + dir[1] * cmd
                x, y = self.search(x, y, cand_x, cand_y, x_obstacles,
                                   y_obstacles, dir)
                print(f"{cmd}: ({x}, {y})")
                ans = max(ans, pow(x, 2) + pow(y, 2))
            elif cmd == -2:
                dir = self.updateDir(dir, cmd)
            elif cmd == -1:
                dir = self.updateDir(dir, cmd)
        return ans


# commands = [4, -2, 8, -2, 10, -1, 4, -1, 10]
# obstacles = [[-4, 4], [-8, 0]]

commands = [-2, -1, -2, 3, 7]
obstacles = [[1, -3], [2, -3], [4, 0], [-2, 5], [-5, 2], [0, 0], [4, -4],
             [-2, -5], [-1, -2], [0, 2]]

print(Solution().robotSim(commands, obstacles))
