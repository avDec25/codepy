from typing import List


class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        ce, cc = a[0], 1
        replacer = 1
        for i in range(1, len(a), 1):
            if a[i] == ce:
                if cc == 1:
                    a[replacer] = ce
                    replacer += 1
                    cc += 1
                elif cc == 2:
                    continue
            else:
                ce, cc = a[i], 1
                a[replacer] = ce
                replacer += 1
        print(a)
        return replacer


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(Solution().removeDuplicates(nums))
