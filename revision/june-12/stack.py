from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        stk = [float("-inf")]
        for temp in temperatures:
            while stk and stk[-1] < temp:
                stk.pop()
            ans.append(len(stk))
            stk.append(temp)
        return ans


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))

temperatures = [30, 40, 50, 60]
print(Solution().dailyTemperatures(temperatures))

temperatures = [30, 60, 90]
print(Solution().dailyTemperatures(temperatures))
