from typing import List
import math

class Solution:
    def minDamage(self, p: int, damage: List[int], health: List[int]) -> int:
        a = [math.ceil(h // p) for h in health]
        f = sorted(zip(a, damage), key=lambda x: (x[1] / x[0]), reverse=True)
        ans = 0
        tot = sum(damage)
        for hit, dam in f:
            ans += tot * hit
            tot -= dam
        return ans


power = 1
damage = [1,1,1,1]
health = [1,2,3,4]

# power = 8
# damage = [40]
# health = [59]

print(Solution().minDamage(power, damage, health))