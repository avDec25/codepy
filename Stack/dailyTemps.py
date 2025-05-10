from typing import List


class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        stk = [[n-1]]
        for i in range(n - 2, 0, -1):
            new_top = []
            for j in stk[-1]:
                if t[i] < t[j]: # will also work for duplicate elements
                    new_top.append(j)
            new_top.append(i)
            stk.append(new_top)

        ans = []
        for i in range(n-1):
            appended = False
            for j in stk[-1][::-1]:
                if t[i] < t[j]:
                    ans.append(j-i)
                    appended = True
                    break
            if not appended:
                ans.append(0)
            stk.pop()
        ans.append(0)
        return ans



temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))

# temperatures = [30, 40, 50, 60]
# print(Solution().dailyTemperatures(temperatures))
#
# temperatures = [30, 60, 90]
# print(Solution().dailyTemperatures(temperatures))
