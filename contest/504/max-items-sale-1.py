from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        if n == 0 or budget <= 0:
            return 0

        min_price = min(item[1] for item in items)

        unlock_masks = [0] * n
        for i in range(n):
            mask = 1 << i
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    mask |= (1 << j)
            unlock_masks[i] = mask


        profits = []
        weights = []
        for i in range(n):
            weights.append(items[i][1])
            count = 1
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    count += 1
            profits.append(count)

        dp = [0] * (budget + 1)

        for i in range(n):
            w_item = weights[i]
            p_item = profits[i]
            for w in range(budget, w_item - 1, -1):
                dp[w] = max(dp[w], dp[w - w_item] + p_item)

        max_total = 0
        for w in range(budget + 1):
            leftover = budget - w
            extra_items = leftover // min_price
            max_total = max(max_total, dp[w] + extra_items)

        return max_total


items = [[6, 2], [2, 6], [3, 4]]
budget = 9
print(Solution().maximumSaleItems(items, budget))

items = [[2, 4], [3, 2], [4, 1], [6, 4], [12, 4]]
budget = 8
print(Solution().maximumSaleItems(items, budget))
