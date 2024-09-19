from typing import List
import heapq


class Solution:
    def longestConsecutive(self, a: List[int]) -> int:
        if not a:
            return 0

        print(sorted(a))

        heapq.heapify(a)
        ans = float('-inf')
        cc = 1
        prev = heapq.heappop(a)
        while a:
            popped = heapq.heappop(a)
            if prev == popped:
                continue
            if abs(popped - prev) == 1:
                cc += 1
            else:
                ans = max(ans, cc)
                cc = 1
            prev = popped
        ans = max(ans, cc)
        return ans


nums = [1, 2, 0, 1]
print(Solution().longestConsecutive(nums))

nums = [100, 4, 200, 1, 3, 2]
print(Solution().longestConsecutive(nums))

nums = [100, 4, 200, 1, 3, 2]
print(Solution().longestConsecutive(nums))

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(Solution().longestConsecutive(nums))

nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
print(Solution().longestConsecutive(nums))
