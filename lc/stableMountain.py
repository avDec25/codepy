from typing import List


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ans = []
        for i in range(1, len(height)):
            if height[i - 1] > threshold:
                ans.append(i)
        return ans


height = [1, 2, 3, 4, 5]
threshold = 2
print(Solution().stableMountains(height, threshold))

height = [10, 1, 10, 1, 10]
threshold = 3
print(Solution().stableMountains(height, threshold))
