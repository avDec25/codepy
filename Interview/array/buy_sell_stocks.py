from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxp = 0
        buy, sell = 0, 1
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                mxp = max(mxp, prices[sell]-prices[buy])
            else:
                buy = sell
            sell += 1
        return mxp

prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))

prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))