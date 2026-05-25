from collections import deque
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        target = tuple(sorted(nums))
        start = tuple(nums)

        if start == target:
            return 0

        q = deque([(start, 0)])
        visited = {start}

        while q:
            state, ops = q.popleft()

            rev = state[::-1]
            if target == rev:
                return ops + 1
            if rev not in visited:
                q.append((rev, ops + 1))
                visited.add(rev)

            rot = state[1:] + state[:1]
            if target == rot:
                return ops + 1
            if rot not in visited:
                q.append((rot, ops + 1))
                visited.add(rot)

        return -1


nums = [0, 2, 1]
print(Solution().minOperations(nums))

nums = [1, 0, 2]
print(Solution().minOperations(nums))

nums = [2, 0, 1, 3]
print(Solution().minOperations(nums))
