import unittest
from typing import List
import math


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        sum_n = mean * (n + m) - sum(rolls)
        ans = []
        subsection = math.floor(sum_n / n)
        if subsection <= 0 or subsection > 6:
            return []

        sm = 0
        for i in range(n):
            ans.append(subsection)
            sm += subsection

        residual = abs(sum_n - sm)
        x = 0
        while residual != 0:
            residual -= 1
            ans[x] += 1
            if ans[x] > 6 or ans[x] <= 0:
                return []
            x += 1

        return ans


class ExampleCasesTests(unittest.TestCase):

    def test_tc1(self):
        rolls = [3, 2, 4, 3]
        mean = 4
        n = 2
        self.assertEqual([6, 6], Solution().missingRolls(rolls, mean, n))

    def test_tc2(self):
        rolls = [1, 5, 6]
        mean = 3
        n = 4
        self.assertListEqual(sorted([2, 2, 2, 3], reverse=True),
                             Solution().missingRolls(rolls, mean, n))

    def test_tc3(self):
        rolls = [1, 2, 3, 4]
        mean = 6
        n = 4
        self.assertEqual([], Solution().missingRolls(rolls, mean, n))

    def test_tc4(self):
        rolls = [6, 3, 4, 3, 5, 3]
        mean = 1
        n = 6
        self.assertEqual([], Solution().missingRolls(rolls, mean, n))

    def test_tc5(self):
        rolls = [3, 5, 3]
        mean = 5
        n = 5
        self.assertEqual([6, 6, 6, 6, 5], Solution().missingRolls(rolls, mean, n))

    def test_tc6(self):
        rolls = [4, 5, 6, 2, 3, 6, 5, 4, 6, 4, 5, 1, 6, 3, 1, 4, 5, 5, 3, 2, 3,
                 5, 3, 2, 1, 5, 4, 3, 5, 1, 5]
        mean = 4
        n = 40
        self.assertEqual(sorted(
            [4, 4, 4, 4, 4, 4, 5, 5, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5,
             4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5],
            reverse=True),
            Solution().missingRolls(rolls, mean, n))

    def test_tc7(self):
        rolls = [4, 2, 2, 5, 4, 5, 4, 5, 3, 3, 6, 1, 2, 4, 2, 1, 6, 5, 4, 2, 3,
                 4, 2, 3, 3, 5, 4, 1, 4, 4, 5, 3, 6, 1, 5, 2, 3, 3, 6, 1, 6, 4,
                 1, 3]
        mean = 2
        n = 53
        self.assertEqual([], Solution().missingRolls(rolls, mean, n))


if __name__ == '__main__':
    unittest.main()
