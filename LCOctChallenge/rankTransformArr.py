from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []
        a = arr.copy()
        a.sort()
        r = 1
        rank = {}
        rank[a[0]] = r
        for i in range(1, len(a)):
            if a[i] == a[i - 1]:
                rank[a[i]] = r
            else:
                r += 1
                rank[a[i]] = r
        ans = []
        for i in range(len(arr)):
            ans.append(rank[arr[i]])
        return ans


arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
print(Solution().arrayRankTransform(arr))

arr = [40, 10, 20, 30]
print(Solution().arrayRankTransform(arr))

arr = [100, 100, 100]
print(Solution().arrayRankTransform(arr))
