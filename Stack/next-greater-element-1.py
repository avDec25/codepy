from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nxt_greater = {}
        stk = []

        for num in reversed(nums2):
            while stk and stk[-1] <= num:
                stk.pop()
            nxt_greater[num] = -1 if not stk else stk[-1]
            stk.append(num)

        return [nxt_greater[num] for num in nums1]


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(Solution().nextGreaterElement(nums1, nums2))

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(Solution().nextGreaterElement(nums1, nums2))
