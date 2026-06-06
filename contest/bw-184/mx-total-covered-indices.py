from typing import List
class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        n = len(nums)
        memo = {}

        def dp(i: int, covered_by_prev: bool) -> int:
            if i < 0:
                return 0

            state = (i, covered_by_prev)
            if state in memo:
                return memo[state]

            if i == 0:
                if covered_by_prev or s[0] == '1':
                    return nums[0]
                return 0

            if covered_by_prev:
                if s[i] == '1':
                    # Choice 1: Move to i-1
                    choice1 = nums[i] + dp(i - 1, True)
                    # Choice 2: Keep at i
                    choice2 = nums[i] + dp(i - 1, False)
                    res = max(choice1, choice2)
                else:
                    res = nums[i] + dp(i - 1, False)
            else:
                if s[i] == '1':
                    # Choice 1: Move to i-1
                    choice1 = dp(i - 1, True)
                    # Choice 2: Keep at i
                    choice2 = nums[i] + dp(i - 1, False)
                    res = max(choice1, choice2)
                else:
                    res = dp(i - 1, False)

            memo[state] = res
            return res

        return dp(n - 1, False)

nums = [9,2,6,1]
s = "0101"
print(Solution().maxTotal(nums, s))

nums = [5,1,4]
s = "001"
print(Solution().maxTotal(nums, s))

nums = [9,3,5]
s = "011"
print(Solution().maxTotal(nums, s))
