from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def next_curr(curr):
            if curr * 10 <= n:
                return curr * 10

            if curr >= n:
                curr //= 10

            curr += 1

            while curr % 10 == 0:
                curr //= 10
            return curr

        ans = []
        curr = 1
        for _ in range(n):
            ans.append(curr)
            curr = next_curr(curr)

        return ans


n = 130
print(Solution().lexicalOrder(n))

n = 2
print(Solution().lexicalOrder(n))
