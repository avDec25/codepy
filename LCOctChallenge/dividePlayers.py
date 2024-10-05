from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total = skill[0] + skill[-1]
        chem = skill[0] * skill[-1]
        for i in range(1, len(skill) // 2):
            if skill[i] + skill[-i-1] != total:
                return -1
            else:
                chem += skill[i] * skill[-i-1]

        return chem


skill = [3, 2, 5, 1, 3, 4]
print(Solution().dividePlayers(skill))

skill = [3, 4]
print(Solution().dividePlayers(skill))

skill = [1, 1, 2, 3]
print(Solution().dividePlayers(skill))
