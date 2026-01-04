from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: # no transaction is possible
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if max_profit < profit:
                    max_profit = profit

        return max_profit

    def maxProfit_v1(self, prices: List[int]) -> int:
        l, r = 0, 1
        mxp = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                mxp = max(mxp, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return mxp


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))

prices = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices))
