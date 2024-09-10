from collections import deque


class Solution:
    def neighbors(self, pos, moves):
        ans = []
        for dice in range(1, 7):
            new_pos = pos + dice
            if new_pos > 30:
                break
            elif moves[new_pos] != -1:
                new_pos = moves[new_pos]
            ans.append(new_pos)
        return ans

    def minThrow(self, N, arr):
        moves = [-1] * 31
        for i in range(0, N*2, 2):
            if arr[i] < arr[i+1]:
                moves[arr[i]] = arr[i + 1]

        q = deque()
        q.append((0, 0))

        visited = set()
        visited.add(0)

        ans = float('inf')
        while q:
            curr, curr_dist = q.popleft()
            if curr == 30: return curr_dist
            for neighbour in self.neighbors(curr, moves):
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append((neighbour, curr_dist + 1))

        return ans


N = 3
# arr = [21, 8, 13, 29, 16, 26]
arr = [3, 22, 5, 8, 11, 26, 20, 29, 17, 4, 19, 7, 27, 1, 29, 9]
print(Solution().minThrow(N, arr))
