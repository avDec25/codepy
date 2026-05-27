from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # a warmer day was found!
            while stk and temperatures[i] > temperatures[stk[-1]]:
                index = stk.pop()
                ans[index] = i - index
            # Some previous days are still waiting to find a warmer future day
            stk.append(i)
        return ans


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))

temperatures = [30, 40, 50, 60]
print(Solution().dailyTemperatures(temperatures))

temperatures = [30, 60, 90]
print(Solution().dailyTemperatures(temperatures))
