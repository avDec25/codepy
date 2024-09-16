class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        n = start ^ goal # exclusive OR
        while n != 0:
            if n & 1: # get only the last bit, ans see if its 1
                ans += 1
            n >>= 1     # shift to right remove that visited bit
        return ans

    def minBitFlips_v1(self, start: int, goal: int) -> int:
        ans = 0
        start = bin(start)[2:]
        goal = bin(goal)[2:]

        sl = len(start)-1
        gl = len(goal)-1

        while sl >= 0 and gl >= 0:
            if start[sl] != goal[gl]:
                ans += 1
            sl -= 1
            gl -= 1

        while sl >= 0:
            if start[sl] != '0':
                ans += 1
            sl -= 1

        while gl >= 0:
            if goal[gl] != '0':
                ans += 1
            gl -= 1
        return ans


if __name__ == '__main__':
    start = 10
    goal = 82
    print(Solution().minBitFlips(start, goal) == 3)

    # start = 10
    # goal = 7
    # print(Solution().minBitFlips(start, goal) == 3)
    #
    # start = 3
    # goal = 4
    # print(Solution().minBitFlips(start, goal) == 3)
