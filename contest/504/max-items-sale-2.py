from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        if n == 0 or budget <= 0:
            return 0

        min_price = min(item[1] for item in items)

        item_bonuses = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    item_bonuses[i] += 1

        knapsack_items = []
        for i in range(n):
            cost = items[i][1]
            for _ in range(item_bonuses[i]):
                knapsack_items.append((cost, 2))

        dp = [0] * (budget + 1)

        for cost, value in knapsack_items:
            for w in range(budget, cost - 1, -1):
                dp[w] = max(dp[w], dp[w - cost] + value)

        max_total = 0
        for w in range(budget + 1):
            leftover_budget = budget - w
            extra_items = leftover_budget // min_price
            max_total = max(max_total, dp[w] + extra_items)

        return max_total