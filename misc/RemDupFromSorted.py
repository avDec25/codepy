from typing import List

class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        curr = a[0]
        replacer = 1
        for i in range(1, len(a), 1):
            if a[i] == curr:
                continue
            else:
                curr = a[i]
                a[replacer] = curr
                replacer += 1
        return replacer


nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))

