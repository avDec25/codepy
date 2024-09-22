from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int],
                 speed: List[int]) -> int:
        ps = [(p, s) for p, s in zip(position, speed)]
        stk = []
        for p, s in sorted(ps)[::-1]:
            stk.append((target - p) / s)

            # if time pf second last is less,
            # then it will bump into the one in the front
            # which means they will merge, hence POP
            if len(stk) >= 2 and stk[-2] >= stk[-1]:
                stk.pop()
        return len(stk)


target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
print(Solution().carFleet(target, position, speed))
