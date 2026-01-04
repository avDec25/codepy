from typing import List
import sys
from collections import defaultdict


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        merged = []
        for i, lst in enumerate(nums):
            for e in lst:
                merged.append((e, i))
        merged.sort()

        result = [-sys.maxsize, sys.maxsize]
        left = 0
        count_list = defaultdict(int)
        unique_lists = 0
        for right in range(len(merged)):
            _, i = merged[right]

            if count_list[i] == 0:
                unique_lists += 1
            count_list[i] += 1

            while unique_lists == len(nums):
                if merged[right][0] - merged[left][0] < result[1] - result[0]:
                    result = [merged[left][0], merged[right][0]]

                left_idx = merged[left][1]
                count_list[left_idx] -= 1
                if count_list[left_idx] == 0:
                    unique_lists -= 1

                left += 1

        return result


nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
print(Solution().smallestRange(nums))
