from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices and len(prices) < 2:
            return 0
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))

prices = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices))
