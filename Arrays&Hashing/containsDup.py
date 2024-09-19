from typing import List


class Solution:
    def containsDuplicate_v1(self, a: List[int]) -> bool:
        freq = dict()
        for e in a:
            if e not in freq:
                freq[e] = 1
            else:
                return True
        return False

    def containsDuplicate(self, a: List[int]) -> bool:
        visited = set()
        for e in a:
            if e in visited:
                return True
            else:
                visited.add(e)
        return False


nums = [1, 2, 3, 1]
print(Solution().containsDuplicate(nums))
nums = [1, 2, 3, 4]
print(Solution().containsDuplicate(nums))
